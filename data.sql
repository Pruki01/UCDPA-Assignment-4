INSERT INTO screens (type) VALUES('Small');
INSERT INTO screens (type) VALUES('Small');
INSERT INTO screens (type) VALUES('Small');
INSERT INTO screens (type) VALUES('Medium');
INSERT INTO screens (type) VALUES('Medium');
INSERT INTO screens (type) VALUES('Medium');
INSERT INTO screens (type) VALUES('Large');
INSERT INTO screens (type) VALUES('Large');
INSERT INTO screens (type) VALUES('Large');

-- password: admin
INSERT INTO users (email, password, is_admin) VALUES(
    'admin@gmail.com',
    'scrypt:32768:8:1$JihKLHxv1ZPfoRyF$c51aa85883c11096212707a6adddb2647002ac98a084fef909e305ee555614bb39a46c92c626927f0a44d3c43b4dbb04ef4ecce4f9cd7a99579ab1ba245164a5',
    true
)

-- Image: https://www.imdb.com/title/tt0111161/mediaviewer/rm1690056449/?ref_=tt_ov_i
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'The Shawshank Redemption',
	'DRAMA',
	'After a banker is sentenced to life in Shawshank Prison, he forms an unlikely friendship with a seasoned inmate and clings to hope amid cruelty and corruption.',
	144,
	'SPECIAL',
	'TheShawshankRedemption.jpg'

)

-- Image: https://www.imdb.com/title/tt0068646/mediaviewer/rm746868224/?ref_=tt_ov_i
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'The Godfather',
	'DRAMA',
	'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
	175,
	'SPECIAL',
	'TheGodfather.jpg'

)

-- Image: https://www.imdb.com/title/tt0468569/mediaviewer/rm4023877632/?ref_=tt_ov_i
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'The Dark Knight',
	'ACTION',
	'When a menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman, James Gordon and Harvey Dent must work together to put an end to the madness.',
	152,
	'SPECIAL',
	'TheDarkKnight.jpg'

)

-- Image: https://www.imdb.com/title/tt0167260/mediaviewer/rm584928512/?ref_=tt_ov_i
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'Lord of the Rings: The Return of the King',
	'ACTION',
	'Gandalf and Aragorn lead the World of Men against Saurons army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.',
	201,
	'SPECIAL',
	'LordOfTheRings.jpg'

)

-- Image: https://www.imdb.com/title/tt0050083/mediaviewer/rm2927108352/?ref_=tt_ov_i
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'12 Angry Men',
	'DRAMA',
	'The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.',
	96,
	'SPECIAL',
	'12AngryMen.jpg'

)

-- Image: https://www.google.com/imgres?q=pulp%20fiction%20cover&imgurl=https%3A%2F%2Fcdng.europosters.eu%2Fpod_public%2F750%2F262754.jpg&imgrefurl=https%3A%2F%2Fwww.europosters.eu%2Fpulp-fiction%2F&docid=wGOSYhCKRxMEmM&tbnid=prEYj3dtat-ijM&vet=12ahUKEwiP7vvU-P-VAxUwVkEAHUQeHGsQnPAOegUInAEQAA..i&w=500&h=750&hcb=2&ved=2ahUKEwiP7vvU-P-VAxUwVkEAHUQeHGsQnPAOegUInAEQAAhttps://en.wikipedia.org/wiki/Pulp_Fiction#/media/File:Pulp_Fiction_(1994)_poster.jpg
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'Pulp Fiction',
	'DRAMA',
	'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
	154,
	'SPECIAL',
	'PulpFiction.jpg'

)