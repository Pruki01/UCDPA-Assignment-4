const seatsContainer    = document.querySelector('.seats');
const seats             = document.querySelectorAll('.row .seat:not(.occupied):not(.empty)');
const btn               = document.querySelector('.tickets-btn');
const form              = document.querySelector('.booking-form');
const selectedSeats     = document.querySelector('#tickets');

console.log(seatsContainer);
console.log(seats);

const rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'];

function getSelectedSeats(){
    
    return_str = '';
    
    [...document.querySelectorAll('.seat.selected')].map(seat => {
        const row = seat.closest('.row');

        const rowIndex = [...document.querySelectorAll('.row')].indexOf(row);
        const seatIndex = [...row.children].indexOf(seat);

        return_str += `${rows[rowIndex]}${seatIndex},`;

    });

    return return_str;
}

seatsContainer.addEventListener('click', e =>{

    console.log(e.target);
    if(e.target.classList.contains('seat') &&
        !e.target.classList.contains('occupied') &&
        !e.target.classList.contains('empty')){

        e.target.classList.toggle('selected');

    }

});

form.addEventListener('submit', () => {

    selectedSeats.value = getSelectedSeats();

});