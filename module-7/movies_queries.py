import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    user='movies_user',
    password='popcorn',
    host='127.0.0.1',
    database= 'movies',
    raise_on_warnings=True
)

# Create a cursor object
cursor = db.cursor()

# Query 1: Select all fields from the studio table
print("-- DISPLAYING Studio RECORDS --")
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

# Query 2: Select all fields from the genre table
print("-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

# Query 3: Select movie names with a runtime of less than two hours
print("-- DISPLAYING Short Film RECORDS --")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
short_films = cursor.fetchall()
for film in short_films:
    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

print("-- DISPLAYING Director RECORDS in Order --")
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
films_directors = cursor.fetchall()
for film in films_directors:
    print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))0

# Close the cursor and connection
cursor.close()
db.close()
