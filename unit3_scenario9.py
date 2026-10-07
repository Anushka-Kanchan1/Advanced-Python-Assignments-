import csv
import re

FILE = "movies.csv"


def load_movies():
    try:
        with open(FILE, "r") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print("File not found!")
        return []


def display_movies(movies):
    for movie in movies:
        print("Movie ID:", movie["ID"])
        print("Title:", movie["Title"])
        print("Year:", movie["Year"])
        print("Rating:", movie["Rating"])
        print("------------------------")


def search_by_id(movies, movie_id):
    for movie in movies:
        if movie["ID"] == movie_id:
            print("\nMovie Found!")
            print("ID:", movie["ID"])
            print("Title:", movie["Title"])
            print("Year:", movie["Year"])
            print("Rating:", movie["Rating"])
            return

    print("Movie not found!")


def search_by_title(movies, title):
    # Regular Expression search
    pattern = re.compile(title, re.IGNORECASE)

    found = False

    for movie in movies:
        if pattern.search(movie["Title"]):
            print("\nMovie Found!")
            print("ID:", movie["ID"])
            print("Title:", movie["Title"])
            print("Year:", movie["Year"])
            print("Rating:", movie["Rating"])
            found = True

    if not found:
        print("Movie not found!")


# Main program
movies = load_movies()

while True:
    print("\n--- Movie Collection System ---")
    print("1. Display All Movies")
    print("2. Search by Movie ID")
    print("3. Search by Title")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_movies(movies)

    elif choice == "2":
        movie_id = input("Enter Movie ID: ")
        search_by_id(movies, movie_id)

    elif choice == "3":
        title = input("Enter movie title: ")
        search_by_title(movies, title)

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
