# Author: Sunil Gupta, Sainithya Surasani, Nihal Reddy Akula.
# Date: 5/5/2024
# Description: Python Project 2 code.


from Book import Book
from Show import Show


import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

# Defining a class Recommender with constructor that instantiates three dictionaries
class Recommender:
    def __init__(self):
        self.__books = {}
        self.__shows = {}
        self.__associations = {}

    # Function to load all the data from a book file
    def loadBooks(self):
        # Asking for file.
        filename = filedialog.askopenfilename(title="Select a file to load books")
        while not filename:
            filename = filedialog.askopenfilename(title="Select a file to load books")
        # Opening the selected file in read mode and iterating through lines in book file.
        with open(filename, 'r') as file:
            file.readline()
            for line in file:
                # Creating Book object and storing it in books dictionary.
                data = line.strip().split(',')
                book = Book(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
                self.__books[data[0]] = book

    # Function to load all the data from a show file
    def loadShows(self):
        # Asking for file.
        filename = filedialog.askopenfilename(title="Select a file to load shows")
        while not filename:
            filename = filedialog.askopenfilename(title="Select a file to load shows")
        # Opening the selected file in read mode and iterating through lines in show file.
        with open(filename, 'r') as file:
            data = file.readline().strip().split(',')
            for line in file:
                # Creating Show object and storing in shows dictionary.
                data = line.strip().split(',')
                show = Show(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12])
                self.__shows[data[0]] = show

    # Function to load all the data from a association file
    def loadAssociations(self):
        # Asking for file.
        filename = filedialog.askopenfilename(title="Select an association file")
        while not filename:
            filename = filedialog.askopenfilename(title="Select an association file")
        # Opening the selected file in read mode and iterating through lines in association file..
        with open(filename, 'r') as file:
            for line in file:
                # Storing association of the show and book in dictionary.
                data = line.strip().split(',')
                id1, id2 = data[0], data[1]
                # Association with id1 as key and id2 as value.
                if id1 not in self.__associations:
                    self.__associations[id1] = {}
                if id2 not in self.__associations[id1]:
                    self.__associations[id1][id2] = 0
                self.__associations[id1][id2] += 1
                # Association with id2 as key and id1 as value.
                if id2 not in self.__associations:
                    self.__associations[id2] = {}
                if id1 not in self.__associations[id2]:
                    self.__associations[id2][id1] = 0
                self.__associations[id2][id1] += 1

    def getMovieList(self):
        """
                Function to return title and runtime of all the stored movies.
               :return: title and runtime of all the stored movies.
               """
        # Calculating the maximum length of title to adjust the columns width based on the length of entries
        max_title_length = 0
        for show in self.__shows.values():
            if show.get_show_type() == "Movie":
                max_title_length = max(max_title_length, len(show.get_title()))

        # Header with appropriate spacing between the columns
        movie_list = []
        header = (f"Title{' ' * (max_title_length - len('Title'))} Runtime")
        movie_list.append(header)

        # Iterating over each show and updating data for movies
        for show in self.__shows.values():
            if show.get_show_type() == "Movie":
                form = f"{show.get_title():<{max_title_length}} {show.get_duration()}"
                movie_list.append(form)
        # return the movie list
        return movie_list

    def getTVList(self):
        """
                    Function to return title and number of seasons for all of the stored tv shows.
                   :return: title and number of seasons of the stored tv shows.
                   """
        # Calculating the maximum length of title to adjust the columns width based on the length of entries
        max_title_length = 0
        for show in self.__shows.values():
            if show.get_show_type() == "TV Show":
                max_title_length = max(max_title_length, len(show.get_title()))

        # Header with appropriate spacing between the columns
        tv_list = []
        header = (f"Title{' ' * (max_title_length - len('Title'))} Seasons")
        tv_list.append(header)

        # Iterating over each show and updating data for tv shows
        for show in self.__shows.values():
            if show.get_show_type() == "TV Show":
                form = f"{show.get_title():<{max_title_length}} {show.get_duration()}"
                tv_list.append(form)
        # return the tv list
        return tv_list

    def getBookList(self):
        """
                Function to return title and author of the stored books.
               :return: title and author of the stored books.
               """
        # Calculating the maximum length of title to adjust the columns width based on the length of entries
        max_title_length = 0
        for book in self.__books.values():
            max_title_length = max(max_title_length, len(book.get_title()))

        # Header with appropriate spacing between the columns
        book_list = []
        header = (f"Title{' ' * (max_title_length - len('Title'))} Author(s)")
        book_list.append(header)

        # Iterating over each book and updating data for books
        for book in self.__books.values():
            form = f"{book.get_title():<{max_title_length}} {book.get_authors()}"
            book_list.append(form)
        # return the book list
        return book_list

    def getMovieStats(self):
        """
            Function to return statistics of the movies.
           :return: movie statistics such as Ratings with rating percentages, average duration,
           most prolific director and actor,frequent genre
           """
        # Dictionaries to store the data of ratings,directors,actors and genres of movies
        ratings = {}
        directors = {}
        actors = {}
        genres = {}
        r_count = 0
        total_duration = 0
        num_movies = 0
        # Iterating through the contents of show dictionary
        for show in self.__shows.values():
            # Storing ratings for movies
            if show.get_show_type() == "Movie":
                # If the rating is not in ratings dictionary, we store it in the dictionary
                # with rating as key and count 1 as value
                if show.get_rating() not in ratings:
                    ratings.update({show.get_rating(): 1})
                    r_count += 1
                # Rating is already in the dictionary, we increment the value of the rating key.
                else:
                    ratings[show.get_rating()] += 1
                    r_count += 1
                num_movies += 1
                # Calculating the total duration of the movies
                duration = show.get_duration()
                duration_parts = duration.split()
                duration_minutes = int(duration_parts[0])
                total_duration += duration_minutes
        # Calculating the average duration of the movies
        average_duration = total_duration / num_movies

        # Iterating through the ratings dictionary and calculating the rating percentage for each rating
        for key, val in ratings.items():
            ratings[key] = (ratings[key] / r_count) * 100

        # Iterating through all shows and storing the directors names of movies and the count in dictionary
        for show in self.__shows.values():
            if show.get_show_type() == "Movie":
                direc = show.get_directors()
                direc = direc.split("\\")
                for i in direc:
                    if i == "":
                        continue
                    if i in directors:
                        directors[i] += 1
                    else:
                        directors[i] = 1
        # Finding the most prolific director among the stored directors
        prolific_director = max(directors, key=directors.get)

        # Iterating through all shows and storing the actor names of movies and the count in dictionary
        for show in self.__shows.values():
            if show.get_show_type() == "Movie":
                actor = show.get_actors()
                actor = actor.split("\\")
                for i in actor:
                    if i == "":
                        continue
                    if i in actors:
                        actors[i] += 1
                    else:
                        actors[i] = 1
        # Finding the most prolific actor among the stored actors
        prolific_actor = max(actors, key=actors.get)

        for show in self.__shows.values():
            if show.get_show_type() == "Movie":
                genre = show.get_genres()
                genre = genre.split("\\")
                for i in genre:
                    if i == "":
                        continue
                    if i in genres:
                        genres[i] += 1
                    else:
                        genres[i] = 1
        # Finding the most frequent genre among the stored genres
        frequent_genre = max(genres, key=genres.get)


        dicti = {"Ratings": {f"{key} {ratings[key]: .2f}%" for key in ratings.keys()},
            "Average Movie Duration": f"{average_duration:.2f} minutes",
            "Most Prolific Director": prolific_director,
            "Most Prolific Actor": prolific_actor,
            "Most Frequent Movie Genre": frequent_genre}

        # Storing the data in list for proper sequential access. After creating list returning the list.
        result = []
        result.append('Ratings')
        for i in dicti['Ratings']:
            result.append(i)
        result.append("")
        result.append(f"Average Movie Duration : {dicti['Average Movie Duration']}")
        result.append("")
        result.append(f"Most Prolific Director : {dicti['Most Prolific Director']}")
        result.append("")
        result.append(f"Most Prolific Actor : {dicti['Most Prolific Actor']}")
        result.append("")
        result.append(f"Most Frequent Movie Genre : {dicti['Most Frequent Movie Genre']}")
        return result


    def getTVStats(self):
        """
                    Function to return statistics of the TV Shows.
                   :return: TV Show statistics such as Ratings with rating percentages, average number of seasons,
                    most prolific actor,and frequent genre.
                   """
        # Dictionaries to store the data of ratings,directors,actors and genres
        ratings = {}
        actors = {}
        genres = {}
        r_count = 0
        total_seasons = 0
        num_tv_shows = 0
        # Iterating through the contents of show dictionary
        for show in self.__shows.values():
            # Storing ratings for tv shows
            if show.get_show_type() == "TV Show":
                # If the rating is not in ratings dictionary, we store it in the dictionary
                # with rating as key and count 1 as value
                if show.get_rating() not in ratings:
                    ratings.update({show.get_rating(): 1})
                    r_count += 1
                # Rating is already in the dictionary, we increment the value of the rating key.
                else:
                    ratings[show.get_rating()] += 1
                    r_count += 1
                num_tv_shows += 1
                # Calculating the total seasons of the tv shows
                seasons = show.get_duration()
                seasons_parts = seasons.split()
                seasons = int(seasons_parts[0])
                total_seasons += seasons
        # Calculating the average number of seasons of the tv shows
        average_num_seasons = total_seasons / num_tv_shows

        # Iterating through the ratings dictionary and calculating the rating percentage for each rating
        for key, val in ratings.items():
            ratings[key] = (ratings[key] / r_count) * 100
        # Iterating through all shows and storing the actor names of tv shows and the count in dictionary
        for show in self.__shows.values():
            if show.get_show_type() == "TV Show":
                actor = show.get_actors()
                actor = actor.split("\\")
                for i in actor:
                    if i == "":
                        continue
                    if i in actors:
                        actors[i] += 1
                    else:
                        actors[i] = 1
        # Finding the most prolific actor among the stored actors
        prolific_actor = max(actors, key=actors.get)
        # Iterating through all shows and storing the genre of tv shows and the count in dictionary
        for show in self.__shows.values():
            if show.get_show_type() == "TV Show":
                genre = show.get_genres()
                genre = genre.split("\\")
                for i in genre:
                    if i == "":
                        continue
                    if i in genres:
                        genres[i] += 1
                    else:
                        genres[i] = 1
        # Finding the most frequent genre among the stored genres
        frequent_genre = max(genres, key=genres.get)

        dicti = {"Ratings": {f"{key} {ratings[key]: .2f}%" for key in ratings.keys()},
            "Average number of seasons": f"{average_num_seasons:.2f} seasons",
            "Most Prolific Actor": prolific_actor,
            "Most Frequent Movie Genre": frequent_genre}

        # Storing the data in list for proper sequential access. After creating list returning the list.
        result = []
        result.append('Ratings')
        for i in dicti['Ratings']:
            result.append(i)
        result.append("")
        result.append(f"Average number of seasons : {dicti['Average number of seasons']}")
        result.append("")
        result.append(f"Most Prolific Actor : {dicti['Most Prolific Actor']}")
        result.append("")
        result.append(f"Most Frequent Movie Genre : {dicti['Most Frequent Movie Genre']}")
        return result

    def getBookStats(self):
        total_pages = 0
        num_books = 0
        # Dictionaries to store the data of authors and publishers
        authors = {}
        publishers = {}
        # Iterating through all the books in book and calculating average number of pages.
        for book in self.__books.values():
            total_pages += int(book.get_pages())
            num_books += 1
        average_pages = total_pages / num_books

        # Iterating through all the books in book and finding most prolific author.
        for book in self.__books.values():
            author = book.get_authors()
            author = author.split("\\")
            for i in author:
                if i == "":
                    continue
                if i in authors:
                    authors[i] += 1
                else:
                    authors[i] = 1
        prolific_author = max(authors, key=authors.get)

        # # Iterating through all the books in book and finding most prolific publisher.
        for book in self.__books.values():
            publisher = book.get_publisher()
            publisher = publisher.split("\\")
            for i in publisher:
                if i == "":
                    continue
                if i in publishers:
                    publishers[i] += 1
                else:
                    publishers[i] = 1
        prolific_publisher = max(publishers, key=publishers.get)

        dicti= {"Average page count": f"{average_pages:.2f} pages",
            "Most Prolific Author": prolific_author,
            "Most Prolific Publisher": prolific_publisher}

        # Storing the data in list for proper sequential access. After creating list returning the list.
        result = []
        result.append(f"Average page count : {dicti['Average page count']}")
        result.append("")
        result.append(f"Most Prolific Author : {dicti['Most Prolific Author']}")
        result.append("")
        result.append(f"Most Prolific Publisher : {dicti['Most Prolific Publisher']}")
        return result


    def searchTVMovies(self, show_type, title=None, director=None, actor=None, genre=None):
        """
                Function to search for Movie/TV Shows which matches with user's input
               :param show_type: Movie/TV Show
               :type show_type: string
               :param title: Title of the Movie/TV show
               :type title: string
               :param director: Director name
               :type director: string
               :param actor: actor name
               :type actor: string
               :param genre: genre of the Movie/TV Show
               :type genre: string
               :return: returns Title, prolific Director, prolific Actor, and frequent Genre
               """
        # Dictionary to store the data of the objects that adhere to the user input
        match_search = {}
        # If the string is neither Movie nor TV Show,spawn a showerror messagebox
        if show_type != "Movie" and show_type != "TV Show":
            messagebox.showerror("Error", "Please select Movie or TV Show as Type.")
            return ["No Results"]

        # If all of them are empty,spawn a showerror messagebox
        if not any([title, director, actor, genre]):
            messagebox.showerror("Error", "Please enter information for Title, Director, Actor, "
                                          "and/or Genre.")
            return ["No Results"]
        else:
            max_title_length = 0
            max_director_length = 0
            max_actor_length = 0
            max_genre_length = 0
            # Iterating through all the shows
            for key, show in self.__shows.items():
                # Storing the data for shows that adhere with user input
                if show_type == show.get_show_type():
                    if (not title or title in show.get_title()) and \
                            (not director or any(
                                dir in show.get_directors().split("\\") for dir in director.split("\\"))) and \
                            (not actor or any(a in show.get_actors().split("\\") for a in actor.split("\\"))) and \
                            (not genre or any(g in show.get_genres().split("\\") for g in genre.split("\\"))):
                        match_search[key] = show

            # Calculating max lengths of stored matched data to adjust the width of the columns
            for key, val in match_search.items():
                max_title_length = max(max_title_length, len(val.get_title()))
                max_director_length = max(max_director_length, len(val.get_directors()))
                max_actor_length = max(max_actor_length, len(val.get_actors()))
                max_genre_length = max(max_genre_length, len(val.get_genres()))

            # Adding header
            result = []
            header = (f"Title{' ' * max(7, (max_title_length - len('Title')))} "
                      f"Director{' ' * max(7, (max_director_length - len('Director')))} "
                      f"Actor{' ' * max(7, (max_actor_length - len('Actor')))} "
                      f"Genre{' ' * (max_genre_length - len('Genre'))}")
            result.append(header)

            # Iterating over each matched show and updating data
            for val in match_search.values():
                form = (f"{val.get_title():<{max(12, max_title_length)}} "
                        f"{val.get_directors():<{max(15, max_director_length)}} "
                        f"{val.get_actors():<{max(12, max_actor_length)}} "
                        f"{val.get_genres():<{max_genre_length}}")
                result.append(form)

            return result

    def searchBooks(self, title=None, author=None, publisher=None):
        """
                    Function to search for book which matches with user's input
                   :param title: Title of the book
                   :type title: string
                   :param author: author name
                   :type author: string
                   :param publisher: publisher of the book
                   :type publisher: string
                   :return: returns title, prolific author, and prolific publisher
                   """
        # Dictionary to store the data of the objects that adhere to the user input
        match_search = {}
        # If all of them are empty,spawn a showerror messagebox
        if not any([title, author, publisher]):
            messagebox.showerror("Error", "Please enter information for Title, Author, and/or Publisher.")
            return ["No Results"]
        max_title_length = 0
        max_author_length = 0
        max_publisher_length = 0
        # Iterating through all the books
        for key, book in self.__books.items():
            # Storing the data for books that adhere with user input
            if (not title or title in book.get_title()) and \
                    (not author or any(a in book.get_authors().split("\\") for a in author.split("\\"))) and \
                    (not publisher or any(p in book.get_publisher().split("\\") for p in publisher.split("\\"))):
                match_search[key] = book

        # Calculating max lengths of stored matched data to adjust the width of the columns
        for key, val in match_search.items():
            max_title_length = max(max_title_length, len(val.get_title()))
            max_author_length = max(max_author_length, len(val.get_authors()))
            max_publisher_length = max(max_publisher_length, len(val.get_publisher()))

        result = []
        # Adding header

        header = (f"Title{' ' * max(7, (max_title_length - len('Title')))} "
                  f"Author{' ' * max(7, (max_author_length - len('Author')))} "
                  f"Publisher{' ' * (max_publisher_length - len('Publisher'))}")
        result.append(header)

        # Iterating over each matched book and updating data
        for val in match_search.values():
            form = (f"{val.get_title():<{max(12, max_title_length)}} "
                    f"{val.get_authors():<{max(13, max_author_length)}} "
                    f"{val.get_publisher():<{max_publisher_length}}")
            result.append(form)

        return result


    def getRecommendations(self, type_data, title):
        '''
        :param type_data: Type of media.
        :type: String
        :param title: Title of the Media.
        :type: String
        :return: Result of the Recommendation.
        '''
        # Checking for Type of media.
        if type_data == "Movie" or type_data == "TV Show":
            id = -1
            # Searching for the id of the given title. If found exiting the loop.
            for i in self.__shows.values():
                tit = i.get_title()
                if tit == title:
                    id = i.get_id()
                    break
            # If id not found then showing error message.
            if id == -1:
                if title == None:
                    title = ""
                messagebox.showwarning("Error", f"There are no Recommendations for title '{title}'.")
                return "No Result"
            else:
                # If id found then returning the details of the associated media.
                result = []
                headers = ["Title:", "Author:", "Average Rating:", "ISBN:", "ISBN13:", "Language Code:", "Pages:", "Rating Count:", "Publication Date:", "Publisher:"]
                # Storing association dictionary in variable association.
                association = self.__associations[id]
                for i in association:
                    # Getting each id of associated media and storing the object of media in variable boo.
                    boo = self.__books[i]
                    stri = ""
                    stri = headers[0]+"\n"+boo.get_title()+"\n"+headers[1]+"\n"+boo.get_authors()+'\n'+headers[2]+"\n"
                    stri = stri + boo.get_avg_rating()+"\n"+headers[3]+"\n"+boo.get_isbn()+"\n"+headers[4]+"\n"+boo.get_isbn13()+"\n"
                    stri = stri + headers[5]+"\n"+boo.get_lang_code()+"\n"+ headers[6]+"\n"+boo.get_pages()+"\n"
                    stri = stri + headers[7]+"\n"+boo.get_num_ratings()+"\n"+headers[8]+"\n"+boo.get_pub_date()+"\n"
                    stri = stri + headers[9]+"\n"+boo.get_publisher()+"\n"
                    # Creating string of each media details and storing it in result list.
                    result.append(stri)
                    result.append('*************************************************************\n')
                result.pop()
                # Returning a single string made by joining the elements in the result list.
                return '\n'.join(result)
        # Checking for Type of media.
        elif type_data == "Books":
            id = -1
            # Searching for the id of the given title. If found exiting the loop.
            for i in self.__books.values():
                tit = i.get_title()
                if tit == title:
                    id = i.get_id()
                    break
            # If id not found then showing error message.
            if id == -1:
                if title == None:
                    title = ""
                messagebox.showwarning("Error", f"There are no Recommendations for title '{title}'.")
                return "No Result"
            else:
                # If id found then returning the details of the associated media.
                result = []
                headers = ["Title:", "Director:", "Cast:", "Average rating:", "Country:", "Date_added:", "Release year:",
                           "Rating:", "Duration:", "Listed in:", "Description:"]
                # Storing association dictionary in variable association.
                association = self.__associations[id]
                for i in association:
                    # Getting each id of associated media and storing the object of media in variable boo.
                    boo = self.__shows[i]
                    stri = ""
                    stri = headers[0] + "\n" + boo.get_title() + "\n" + headers[1] + "\n" + boo.get_directors() + '\n'
                    stri = stri + headers[2] + "\n" + boo.get_actors() + "\n" + headers[3] + "\n" + boo.get_avg_rating() + "\n"
                    stri = stri + headers[4] + "\n" + boo.get_country_code() + "\n" + headers[5] + "\n" + boo.get_added_date()
                    stri = stri + "\n" + headers[6] + "\n" + boo.get_release_year() + "\n" + headers[7] + "\n"
                    stri = stri + boo.get_rating() + "\n" + headers[8] + "\n" + boo.get_duration() + "\n" + headers[9]
                    stri = stri + "\n" + boo.get_genres() + "\n" + headers[10] + "\n" + boo.get_description() + "\n"
                    # Creating string of each media details and storing it in result list.
                    result.append(stri)
                    result.append('*************************************************************\n')
                result.pop()
                # Returning a single string made by joining the elements in the result list.
                return '\n'.join(result)
        else:
            # Showing error message in case the media Type is not selected.
            messagebox.showwarning("Error", f"Please select Movie, TV Show or Books as Type.")
            return "No Results"
