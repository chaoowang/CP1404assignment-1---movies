"""
Replace the contents of this module docstring with your own details
Name:Chao-Hsuan Wang
Date started: 6, Dec, 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-1---movies-chaoowang
"""

from operator import itemgetter

menu = "Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit"


def main():
    print("Movies To Watch 1.0 - by Chao-Hsuan Wang")

    movie_file = open("movies.csv", "r+")   #open movie for read and write

    movie_list = []
    number_of_line = 0
    movie_index = 0

    lines = movie_file.readlines()         #read all lines in movie file
    for line in lines:
        movie = line.split(",")
        movie[1] = int(movie[1])        #convert year into int
        if movie[3] == "u\n":
            movie[3] = "*"              # "*"=to watch; " "=watched
        else:
            movie[3] = " "
        movie_list.append(movie)
        number_of_line += 1             #count how many movies loaded
    movie_list.sort(key=itemgetter(1, 2))
    for movie in movie_list:            #add movie number
        movie.insert(0, movie_index)
        movie_index += 1

    print("{} movies loaded".format(number_of_line))

    print(menu)
    menu_choice = input("").lower()

    while menu_choice != "q":
        while menu_choice not in ["l", "a", "w","q"]:   #error checking for menu choice
            print("Invalid menu choice")
            print(menu)
            menu_choice = input("").lower()
        if menu_choice == "l":      #list movies
            movie_to_watch = 0
            num_movie_watched = 0
            for line in movie_list:
                print("{}. {} {:<35} - {:>4} ({})".format(line[0], line[4], line[1], line[2], line[3]))
                if line[4] == "*":         #count how many movies watched and how many to watch
                    movie_to_watch += 1
                else:
                    num_movie_watched += 1
            print("{} movies watched, {} movies still to watch".format(num_movie_watched, movie_to_watch))
            print(menu)
            menu_choice = input("").lower()

        elif menu_choice == "a":        #add new movie including: title, year, category
            movie_title = input("Title:")
            while movie_title == "":            #error checking for title
                print("Input can not be blank")
                movie_title = input("Title:")

            movie_year = input("Year:")
            year_check=False
            while year_check==False:        #error checking for year
                try:
                    movie_year=int(movie_year)
                    if movie_year < 0:
                        print("Number must be >= 0")
                        movie_year=input("Year:")
                    else:
                        year_check = True
                except ValueError:
                    print("Invalid input; enter a valid number")
                    movie_year=input("Year:")

            movie_category = input("Category:")
            while movie_category == "":         #error checking for category
                print("Input can not be blank")
                movie_category = input("Category")

            movie_list.append([movie_index, movie_title, movie_year, movie_category, "*"]) #add new movie to movie list
            print("{} ({} from {}) added to movie list".format(movie_title,movie_category,movie_year))
            movie_index+=1

            for movie in movie_list:                #reorder movies after new movie added
                movie.pop(0)                        #remove old movie number
            movie_list.sort(key=itemgetter(1, 2))   #resort movies
            new_index=0
            for movie in movie_list:                #add new new movie number
                movie.insert(0,new_index)
                new_index+=1

            print(menu)
            menu_choice = input("").lower()

        elif menu_choice == "w":        #watch a movie
            #TODO: print no more movies to watch when no more movies to watch
            print("Enter the number of movie to mark as watched")
            movie_watched=input()
            while not movie_watched.isdigit():
                #TODO: error checking for negative number
                print("Invalid input; enter a valid number")
                movie_watched=input("")
            while int(movie_watched)>=len(movie_list):
                print("Invalid movie number")
                movie_watched=input("")
            for movie in movie_list:
                if int(movie_watched)==movie[0]:
                    if movie[4]==" ":
                        print("You have already watched {}".format(movie[1]))
                    else:
                        print("{} from {} watched".format(movie[1],movie[2]))
                        movie[4]=" "
            print(menu)
            menu_choice = input("").lower()
        elif menu_choice=="q":
            pass
    print("Quit")
    # TODO: save movie.csv


if __name__ == '__main__':
    main()
