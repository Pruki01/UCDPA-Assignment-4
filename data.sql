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

-- Image: https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTcWb6EgdTNmBnimW_uauDxf0y1jsmmVlMmiboVZDd05ZlxnqnQhttps://www.instagram.com/p/DNDxGPXiZdn/
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'Spider-Man: Brand New Day',
	'ACTION',
	'A forgotten Peter Parker lives alone as a full-time Spider-Man until mounting pressure triggers a dangerous change and a powerful new enemy emerges.',
	145,
	'CURRENT',
	'Spider-Man.jpg'

)

-- Image: https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQRK4B5d2j1ei8XiwWtOBo-HT0YHpyUqttdx_ls1d49Z-oIfGyv
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'The Odyssey (2026)',
	'ACTION',
	'After the Trojan War, Odysseus faces a dangerous voyage back to Ithaca, meeting creatures like the Cyclops Polyphemus, Sirens, and Calypso along the way.',
	145,
	'CURRENT',
	'TheOdyssey.jpg'

)

-- Image: https://www.google.com/imgres?q=toy%20story%205&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2F0%2F08%2FToy_Story_5_poster.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FToy_Story_5&docid=YC3X2EQvqcRbHM&tbnid=7wj7lk9RYLA6fM&vet=12ahUKEwi9ksGp-v-VAxXhVUEAHe1RLlQQnPAOegQIMhAA..i&w=260&h=385&hcb=2&ved=2ahUKEwi9ksGp-v-VAxXhVUEAHe1RLlQQnPAOegQIMhAA
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'Toy Story 5',
	'DRAMA',
	'Woody, Buzz, Jessie and the rest of the gang jobs are challenged when theyre introduced to electronics, a new threat to playtime.',
	102,
	'CURRENT',
	'ToyStory5.jpg'

)

-- Image: https://www.google.com/imgres?q=evil%20dead%20burn&imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BZTljMTZjZTItZjMzZi00NDBhLWFmMzAtOGNiNTlhY2MxMzg5XkEyXkFqcGc%40._V1_QL75_UX190_CR0%2C0%2C190%2C281_.jpg&imgrefurl=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt31170389%2F&docid=Zn5i8KwYZLrNLM&tbnid=LagY9Caw4Aby6M&vet=12ahUKEwj4oMz3-v-VAxVEUUEAHTUWEwEQnPAOegQIPxAA..i&w=190&h=281&hcb=2&itg=1&ved=2ahUKEwj4oMz3-v-VAxVEUUEAHTUWEwEQnPAOegQIPxAA
INSERT INTO movies (title, genre, description, duration, status, image) VALUES
(
	'Evil Daed Burn',
	'HORROR',
	'After the loss of her husband, a woman seeks solace with her in-laws. As one by one they transform into deadites, she comes to discover that the vows she took in life - survive even in death.',
	110,
	'CURRENT',
	'EvilDeadBurn.jpg'

)

INSERT INTO screenings (movie_id, screen_id, date, time) VALUES(
	1,
	1,
	'2026-10-23',
	'19:30:00'
);

INSERT INTO screenings (movie_id, screen_id, date, time) VALUES(
	1,
	1,
	'2026-10-23',
	'17:00:00'
);

INSERT INTO screenings (movie_id, screen_id, date, time) VALUES(
	1,
	1,
	'2026-10-23',
	'14:00:00'
);

INSERT INTO screenings (movie_id, screen_id, date, time) VALUES(
	1,
	1,
	'2026-10-23',
	'11:00:00'
);

INSERT INTO screenings (movie_id, screen_id, date, time) VALUES(
	1,
	2,
	'2026-10-23',
	'20:45:00'
);

INSERT INTO screenings (movie_id, screen_id, date, time) VALUES(
	1,
	2,
	'2026-10-23',
	'18:00:00'
);

INSERT INTO screenings (movie_id, screen_id, date, time) VALUES(
	1,
	6,
	'2026-10-24',
	'14:10:00'
);

INSERT INTO screenings (movie_id, screen_id, date, time) VALUES(
	1,
	6,
	'2026-10-24',
	'11:20:00'
);

INSERT INTO screenings (movie_id, screen_id, date, time) VALUES(
	1,
	9,
	'2026-10-24',
	'21:35:00'
);