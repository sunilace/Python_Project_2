from Book import Book
from Show import Show


import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

class Recommender:
    def __init__(self):
        self.books = {}
        self.shows = {}
        self.associations = {}


    def loadBooks(self):
        filename = filedialog.askopenfilename(title="Select a file to load books")
        while not filename:
            filename = filedialog.askopenfilename(title="Select a file to load books")
        with open(filename, 'r') as file:
            file.readline()
            for line in file:
                data = line.strip().split(',')
                book = Book(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
                self.books[data[0]] = book


    def loadShows(self):
        filename = filedialog.askopenfilename(title="Select a file to load shows")
        while not filename:
            filename = filedialog.askopenfilename(title="Select a file to load shows")
        with open(filename, 'r') as file:
            data = file.readline().strip().split(',')
            for line in file:
                data = line.strip().split(',')
                show = Show(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12])
                self.shows[data[0]] = show


    def loadAssociations(self):
        filename = filedialog.askopenfilename(title="Select an association file")
        while not filename:
            filename = filedialog.askopenfilename(title="Select an association file")
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                id1, id2 = data[0], data[1]
                if id1 not in self.associations:
                    self.associations[id1] = {}
                if id2 not in self.associations[id1]:
                    self.associations[id1][id2] = 0
                self.associations[id1][id2] += 1
                if id2 not in self.associations:
                    self.associations[id2] = {}
                if id1 not in self.associations[id2]:
                    self.associations[id2][id1] = 0
                self.associations[id2][id1] += 1


    def getMovieList(self):
        """
                Function to return title and runtime of all the stored movies.
               :return: title and runtime of all the stored movies.
               """
        # Calculating the maximum length of title to adjust the columns width based on the length of entries
        max_title_length = 0
        for show in self.shows.values():
            if show.get_show_type() == "Movie":
                max_title_length = max(max_title_length, len(show.get_title()))

        # Header with appropriate spacing between the columns
        movie_list = []
        header = (f"Title{' ' * (max_title_length - len('Title'))} Runtime")
        movie_list.append(header)

        # Iterating over each show and updating data for movies
        for show in self.shows.values():
            if show.get_show_type() == "Movie":
                form = f"{show.get_title():<{max_title_length}} {show.get_duration()}"
                movie_list.append(form)

        return movie_list

    def getTVList(self):
        """
                    Function to return title and number of seasons for all of the stored tv shows.
                   :return: title and number of seasons of the stored tv shows.
                   """
        # Calculating the maximum length of title to adjust the columns width based on the length of entries
        max_title_length = 0
        for show in self.shows.values():
            if show.get_show_type() == "TV Show":
                max_title_length = max(max_title_length, len(show.get_title()))

        tv_list = []
        header = (f"Title{' ' * (max_title_length - len('Title'))} Seasons")
        tv_list.append(header)

        # Iterating over each show and updating data for movies
        for show in self.shows.values():
            if show.get_show_type() == "TV Show":
                form = f"{show.get_title():<{max_title_length}} {show.get_duration()}"
                tv_list.append(form)

        return tv_list

    def getBookList(self):
        """
                Function to return title and author of the stored books.
               :return: title and author of the stored books.
               """
        # Calculating the maximum length of title to adjust the columns width based on the length of entries
        max_title_length = 0
        for book in self.books.values():
                max_title_length = max(max_title_length, len(book.get_title()))

        book_list = []
        header = (f"Title{' ' * (max_title_length - len('Title'))} Author(s)")
        book_list.append(header)

        # Iterating over each show and updating data for movies
        for book in self.books.values():
            form = f"{book.get_title():<{max_title_length}} {book.get_authors()}"
            book_list.append(form)

        return book_list

    def getMovieStats(self):
        ratings = {}
        directors = {}
        actors = {}
        genres = {}
        r_count = 0
        total_duration = 0
        num_movies = 0
        # Iterating through the contents of show dictionary
        for show in self.shows.values():
            if show.get_show_type() == "Movie":
                if show.get_rating() not in ratings:
                    ratings.update({show.get_rating(): 1})
                    r_count += 1
                else:
                    ratings[show.get_rating()] += 1
                    r_count += 1
                num_movies += 1
                duration = show.get_duration()
                duration_parts = duration.split()
                duration_minutes = int(duration_parts[0])
                total_duration += duration_minutes
        average_duration = total_duration/num_movies

        for key, val in ratings.items():
            ratings[key] = (ratings[key]/r_count)*100

        for show in self.shows.values():
            if show.get_show_type() == "Movie":
                direc = show.get_directors()
                direc = direc.split("\\")
                for i in direc:
                    if i == "":
                        continue
                    if i in directors:
                        directors[i] +=1
                    else:
                        directors[i] = 1
        prolific_director = max(directors, key=directors.get)

        for show in self.shows.values():
            if show.get_show_type() == "Movie":
                actor = show.get_actors()
                actor = actor.split("\\")
                for i in actor:
                    if i == "":
                        continue
                    if i in actors:
                        actors[i] +=1
                    else:
                        actors[i] = 1
        prolific_actor = max(actors, key=actors.get)

        for show in self.shows.values():
            if show.get_show_type() == "Movie":
                genre = show.get_genres()
                genre = genre.split("\\")
                for i in genre:
                    if i == "":
                        continue
                    if i in genres:
                        genres[i] +=1
                    else:
                        genres[i] = 1
        frequent_genre = max(genres, key=genres.get)

        return {
        "Ratings": {f"{key} {ratings[key]: .2f}%" for key in ratings.keys()},
        "Average Movie Duration": f"{average_duration:.2f} minutes",
        "Most Prolific Director": prolific_director,
        "Most Prolific Actor": prolific_actor,
        "Most Frequent Movie Genre": frequent_genre}


    def getTVStats(self):
        ratings = {}
        actors = {}
        genres = {}
        r_count = 0
        total_seasons = 0
        num_tv_shows = 0
        # Iterating through the contents of show dictionary
        for show in self.shows.values():
            if show.get_show_type() == "TV Show":
                if show.get_rating() not in ratings:
                    ratings.update({show.get_rating(): 1})
                    r_count += 1
                else:
                    ratings[show.get_rating()] += 1
                    r_count += 1
                num_tv_shows += 1
                seasons = show.get_duration()
                seasons_parts = seasons.split()
                seasons = int(seasons_parts[0])
                total_seasons += seasons
        average_num_seasons = total_seasons / num_tv_shows

        for key, val in ratings.items():
            ratings[key] = (ratings[key] / r_count) * 100

        for show in self.shows.values():
            if show.get_show_type() == "TV Show":
                actor = show.get_actors()
                actor = actor.split("\\")
                for i in actor:
                    if i == "":
                        continue
                    if i in actors:
                        actors[i] +=1
                    else:
                        actors[i] = 1
        prolific_actor = max(actors, key=actors.get)

        for show in self.shows.values():
            if show.get_show_type() == "TV Show":
                genre = show.get_genres()
                genre = genre.split("\\")
                for i in genre:
                    if i == "":
                        continue
                    if i in genres:
                        genres[i] +=1
                    else:
                        genres[i] = 1
        frequent_genre = max(genres, key=genres.get)

        return {
            "Ratings": {f"{key} {ratings[key]: .2f}%" for key in ratings.keys()},
            "Average number of seasons": f"{average_num_seasons:.2f} minutes",
            "Most Prolific Actor": prolific_actor,
            "Most Frequent Movie Genre": frequent_genre}

    def getBookStats(self):
        total_pages = 0
        num_books = 0
        authors = {}
        publishers = {}
        for book in self.books.values():
            total_pages += int(book.get_pages())
            num_books += 1
        average_pages = total_pages/num_books

        for book in self.books.values():
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

        for book in self.books.values():
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

        return {
            "Average page count": f"{average_pages:.2f} pages",
            "Most Prolific Author": prolific_author,
            "Most Prolific Publisher": prolific_publisher}

    def searchTVMovies(self,show_type, title=None, director=None, actor=None, genre=None):
        match_search = {}
        if show_type != "Movie" and show_type != "TV Show":
            messagebox.showerror("Error", "Please select Movie or TV Show as Type.")
            return "No Results"

        if not any([title, director, actor, genre]):
            messagebox.showerror("Error", "Please enter information for Title, Director, Actor, "
                                          "and/or Genre.")
            return "No Results"
        else:
            max_title_length = 0
            max_director_length = 0
            max_actor_length = 0
            max_genre_length = 0
            for key,show in self.shows.items():
                if show_type == show.get_show_type():
                    if(not title or title in show.get_title()) and \
                    (not director or any(dir in show.get_directors().split("\\") for dir in director.split("\\"))) and \
                    (not actor or any(a in show.get_actors().split("\\") for a in actor.split("\\"))) and \
                    (not genre or any(g in show.get_genres().split("\\") for g in genre.split("\\"))):
                        match_search[key] = show

            for key,val in match_search.items():
                max_title_length = max(max_title_length, len(val.get_title()))
                max_director_length = max(max_director_length, len(val.get_directors()))
                max_actor_length = max(max_actor_length, len(val.get_actors()))
                max_genre_length = max(max_genre_length, len(val.get_genres()))

            result = []
            header = (f"Title{' ' * max(7,(max_title_length-len('Title')))} "
                      f"Director{' ' * max(7, (max_director_length-len('Director')))} "
                      f"Actor{' ' * max(7,(max_actor_length-len('Actor')))} "
                      f"Genre{' ' * (max_genre_length-len('Genre'))}")
            result.append(header)

            # Iterating over each show and updating data for movies
            for val in match_search.values():
                form = (f"{val.get_title():<{max(12,max_title_length)}} "
                   f"{val.get_directors():<{max(15, max_director_length)}} "
                   f"{val.get_actors():<{max(12, max_actor_length)}} "
                   f"{val.get_genres():<{max_genre_length}}")
                result.append(form)

            return result

    def searchBooks(self,title=None, author=None, publisher=None):
        match_search = {}
        if not any([title, author, publisher]):
            messagebox.showerror("Error", "Please enter information for Title, Author, and/or Publisher.")
            return "No Results"
        max_title_length = 0
        max_author_length = 0
        max_publisher_length = 0
        for key, book in self.books.items():
            if (not title or title in book.get_title()) and \
                        (not author or any(a in book.get_authors().split("\\") for a in author.split("\\"))) and \
                        (not publisher or any(p in book.get_publisher().split("\\") for p in publisher.split("\\"))):
                    match_search[key] = book

        for key, val in match_search.items():
            max_title_length = max(max_title_length, len(val.get_title()))
            max_author_length = max(max_author_length, len(val.get_authors()))
            max_publisher_length = max(max_publisher_length, len(val.get_publisher()))

        result = []
        header = (f"Title{' ' * max(7, (max_title_length - len('Title')))} "
                  f"Author{' ' * max(7, (max_author_length - len('Author')))} "
                  f"Publisher{' ' * (max_publisher_length - len('Publisher'))}")
        result.append(header)

        # Iterating over each show and updating data for movies
        for val in match_search.values():
            form = (f"{val.get_title():<{max(12, max_title_length)}} "
                    f"{val.get_authors():<{max(13, max_author_length)}} "
                    f"{val.get_publisher():<{max_publisher_length}}")
            result.append(form)

        return result








