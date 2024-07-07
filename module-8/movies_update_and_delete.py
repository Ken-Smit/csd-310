import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    "user": 'movies_user',
    "password": 'popcorn',
    "host": '127.0.0.1',
    "database": 'movies',
    'raise_on_warnings': True
}

def show_films(cursor, title):
    # Execute an inner join on all tables
    cursor.execute(
        "SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' "
        "FROM film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id"
    )

    films = cursor.fetchall()

    print("\n -- {} --".format(title))
    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre: {film[2]}\nStudio Name: {film[3]}\n")

# Connect to the database
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Display films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new record into the film table
    add_film = (
        "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) "
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )
    film_data = ("Us", "2019", 116, "Jordan Peele", 2, 1)  # Use only the year for film_releaseDate
    cursor.execute(add_film, film_data)
    cnx.commit()

    # Display films after insertion
    show_films(cursor, "DISPLAYING FILMS AFTER INSERTION")

    # Update the film Alien to being a Horror film
    update_film = "UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'"  # Adjust genre_id as needed
    cursor.execute(update_film)
    cnx.commit()

    # Display films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    # Delete the movie Gladiator
    delete_film = "DELETE FROM film WHERE film_name = 'Gladiator'"
    cursor.execute(delete_film)
    cnx.commit()

    # Display films after deletion
    show_films(cursor, "DISPLAYING FILMS AFTER DELETION")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor.close()
    cnx.close()
