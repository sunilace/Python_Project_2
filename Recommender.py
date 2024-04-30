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
        movie_list = f"Title{' ' * (max_title_length - len('Title') + 5)}Runtime\n"

        # Iterating over each show and updating data for movies
        for show in self.shows.values():
            if show.get_show_type() == "Movie":
                # Left-alignment of the title and runtime of movies within their respective columns
                movie_list += (f"{show.get_title()}{' ' * (max_title_length - len(show.get_title()) + 5)}"
                               f"{show.get_duration()}\n")

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

        # Header with appropriate spacing between the columns
        tv_list = f"Title{' ' * (max_title_length - len('Title') + 5)}Seasons\n"

        # Iterating over each show and updating data for TV shows
        for show in self.shows.values():
            if show.get_show_type() == "TV Show":
                # Left-alignment of the title and runtime of movies within their respective columns
                tv_list += (f"{show.get_title()}{' ' * (max_title_length - len(show.get_title()) + 5)}"
                               f"{show.get_duration()}\n")
        print(tv_list)

    def getBookList(self):
        """
                Function to return title and author of the stored books.
               :return: title and author of the stored books.
               """
        # Calculating the maximum length of title to adjust the columns width based on the length of entries
        max_title_length = 0
        for book in self.books.values():
                max_title_length = max(max_title_length, len(book.get_title()))

        # Header with appropriate spacing between the columns
        book_list = f"Title{' ' * (max_title_length - len('Title') + 5)}Author(s)\n"

        # Iterating over each book and updating data for books
        for book in self.books.values():
            # Left-alignment of the title and author(s) within their respective columns
            book_list += (f"{book.get_title()}{' ' * (max_title_length - len(book.get_title()) + 5)}"
                          f"{book.get_authors()}\n")

        return book_list


