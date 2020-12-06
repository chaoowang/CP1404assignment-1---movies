"""
Replace the contents of this module docstring with your own details
Name:Chao-Hsuan Wang
Date started: 6, Dec, 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-1---movies-chaoowang
"""
menu="Menu:\nL - List movies\nA - Add movies\nW - Watch a movie\nQ - Quit"

def main():
    print("Movies To Watch 1.0 - by Chao-Hsuan Wang")

    movie_file=open("movies.csv", "r+")

    number_of_line=0
    for line in movie_file:
        number_of_line+=1
    print("{} movie loaded".format(number_of_line))

    print(menu)
    menu_choice=input("").lower()

    while menu_choice != "l"and menu_choice!="a"and menu_choice!="w"and menu_choice!="q":
        print("Invalid menu choice")
        print(menu)
        menu_choice=input("")

    while menu_choice!="q":
        if menu_choice=="l":
            print("List movies")
            #TODO: list movies by year than by title
        elif menu_choice=="a":
            print("Add movies")
            #TODO: add movie including Title, Year, Category
        elif menu_choice=="w":
            print("Watch a movie")
            #TODO: mark movie as watched
        print(menu)
        menu_choice=input("")
    print("Quit")
    #TODO: save movie.csv
if __name__ == '__main__':
    main()
