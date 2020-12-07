"""
Replace the contents of this module docstring with your own details
Name:Chao-Hsuan Wang
Date started: 6, Dec, 2020
GitHub URL: https://github.com/JCUS-CP1404/assignment-1---movies-chaoowang
"""

from operator import itemgetter
menu="Menu:\nL - List movies\nA - Add movies\nW - Watch a movie\nQ - Quit"

def main():
    print("Movies To Watch 1.0 - by Chao-Hsuan Wang")

    movie_file=open("movies.csv", "r+")

    movie_list=[]
    number_of_line=0
    movie_index=0
    movie_to_watch=0
    movie_watched=0

    lines=movie_file.readlines()
    for line in lines:
        movie = line.split(",")
        movie[1]=int(movie[1])
        if movie[3]=="u\n":
            movie[3]="*"
        else:
            movie[3]=" "
        movie_list.append(movie)
        number_of_line += 1
    movie_list.sort(key=itemgetter(1,2))
    for movie in movie_list:
        movie.insert(0, movie_index)
        movie_index+=1

    print("{} movies loaded".format(number_of_line))

    print(menu)
    menu_choice=input("").lower()

    while menu_choice != "l"and menu_choice!="a"and menu_choice!="w"and menu_choice!="q":
        print("Invalid menu choice")
        print(menu)
        menu_choice=input("")

    while menu_choice!="q":
        if menu_choice=="l":
            for line in movie_list:
                print("{}. {} {:<35} - {:>4} ({})".format(line[0],line[4],line[1],line[2],line[3]))
                if line[4]=="*":
                    movie_to_watch+=1
                else:
                    movie_watched+=1
            print("{} movies watched, {} movies still to watch".format(movie_watched,movie_to_watch))
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
