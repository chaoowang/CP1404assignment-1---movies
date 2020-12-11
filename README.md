# CP1404 Assignment 1 - Movies To Watch
Assignment 1 for CP1404/CP1804/CP5632, IT@JCU

By: Chao-Hsuan Wang

My assignment details:
    My assignment contain seven functions: load_file(movie_file), count_movies_watch(movie_list), list_movie(movie_list, movie_to_watch, num_movie_watched), add_movie(movie_index, movie_list), resort_movies(movie_list), watch_a_movie(movie_list, movie_to_watch), save_to_file(output_movie_file, movie_list).
    load_file(movie_file) reads the movie.csv and add movie number(index) after sorted by year then by title, the function also count how many movie loaded.
    count_movies_watch(movie_list) counts how many movie watched/unwatched.
    list_movie(movie_list,movie_to_watch,num_movie_watched) list movies.
    add_movie(movie_index, movie_list) add movie title, year and category.
    resort_movies(movie_list) resort the movie after add a movie.
    watch_a_movie(movie_list, movie_to_watch) mark movie as watched.
    save_to_file(output_movie_file, movie_list) save the movies in to csv file.
    Error checking is added for each input.
    Menu choice handel both upper and lower case, by add .lower to the input.


1. How long did the entire project (assignment 1) take you?
        The project takes me two days to finish. 
        The first day I spent about five hours to add menu choices, sort movies list movies, add movies, watch a movie and then check what to do next.
        At the second day I spent three and a half hours fix the error checking for add movie and watch a movie, and refactor some code into function.

2. What do you plan to do  differently in your development process for assignment 2?
        This time I only add TODO at the end of the first day, next time I plan to add TODO at the beginning. 
