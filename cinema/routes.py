from flask import render_template, redirect, flash, url_for, request, jsonify
from flask_login import current_user, login_user, logout_user
from cinema.models import User, Movie, MovieStatus, MovieGenre, Screen, ScreenType, Screening, Order, Ticket, TicketType, TicketPrice
from cinema.forms import LoginForm, RegistrationForm, AddMovieForm, AddScreeningForm, AddTickets
from app import app, session
from werkzeug.utils import secure_filename
import os, datetime

@app.route('/')
def index():

    current_movies  = session.query(Movie).filter(Movie.status == MovieStatus.CURRENT).all()
    special_movies  = session.query(Movie).filter(Movie.status == MovieStatus.SPECIAL).all()
    upcoming_movies = session.query(Movie).filter(Movie.status == MovieStatus.UPCOMING).all()

    return render_template('index.html', title='Star Movies!', 
                           current_movies=current_movies, 
                           special_movies=special_movies, 
                           upcoming_movies=upcoming_movies)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():

        user = session.query(User).filter(User.email == form.email.data).one()

        if user is None or not user.check_password(form.password.data):

            flash('Invalid username or password!')
            return redirect(url_for('login'))


        login_user(user, form.remember_me.data)
        return redirect(url_for('index'))

    else:
        print(form.errors)

    return render_template('auth/login.html', title='Log In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        new_user = User(email=form.email.data)
        new_user.set_password(form.password.data)
        session.add(new_user)
        session.commit()
        login_user(new_user)
        return redirect(url_for('index'))

    else:
        print(form.errors)

    return render_template ('auth/registration.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/movies/add', methods=['GET', 'POST'])
def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit():
        file = form.file.data
        print(file)
        print(app.config['UPLOAD_PATH'])
        print(os.path.exists(app.config['UPLOAD_PATH']))
        file.save(os.path.join(
                    app.config['UPLOAD_PATH'],
                    secure_filename(file.filename)
                    ))

        new_movie = Movie(
            title=form.title.data,
            genre=MovieGenre(form.genre.data),
            duration=form.duration.data,
            status=MovieStatus(form.status.data),
            image=file.filename
        )

        session.add(new_movie)
        session.commit()

    return render_template('movies/add_form.html', title='Add Movie', form=form)

@app.route('/movie/<int:id>')
def movie_view(id):

    movie = session.get(Movie, id)

    for screening in movie.screenings:
        print(screening.time)
        print(screening.screen.type)

    return render_template('movies/movie.html', movie=movie)

@app.route('/movie/edit/<int:id>')
def edit_movie(id):

    movie = session.get(Movie, id)
    form = AddMovieForm(obj=movie)
    return render_template('movies/edit_movie.html', form=form)

@app.route('/movie/screenings/add', methods=['GET', 'POST'])
def add_screening():
    form = AddScreeningForm()
    print(form)

    if form.validate_on_submit():

        selected_screen = session.get(Screen, form.screen.data)
        selected_movie  = session.get(Movie, form.movie.data)

        new_screening = Screening(
            movie_id = selected_movie.id,
            screen_id = selected_screen.id,
            date = form.date.data,
            time = form.time.data
        )
        
        session.add(new_screening)
        session.commit()

        return redirect(url_for('index')) 

    return render_template('movies/add_screening.html', form=form)

@app.route('/screening/<int:id>', methods=['GET', 'POST'])
def buy_tickets(id):
    form = AddTickets()

    screening = session.get(Screening, id)
    template = screening.screen.type.value.lower() + '.html'

    if form.validate_on_submit():

        order = Order(
            user_id=current_user.id
        )
        session.add(order)
        session.flush()

        seats = form.tickets.data
        tickets = seats.split(',')[:-1]

        for ticket in tickets:
            print(ticket)
            new_ticket = Ticket(
                screening=screening,
                order=order,
                ordered=datetime.datetime.now(),
                type=TicketType.ADULT,
                seat=ticket,
                price=TicketPrice.ADULT.value
            )
            session.add(new_ticket)

        session.commit()
        return redirect(url_for('index'))

    return render_template(f'screens/{template}', form=form)
