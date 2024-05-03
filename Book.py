# Author: Sunil Gupta, Sainithya Surasani, Nihal Reddy Akula.
# Date: 5/5/2024
# Description: Python Project 2 code.


from Media import Media

class Book(Media):
    # Constructer function.
    def __init__(self, media_id, title, authors, avg_rating, isbn, isbn13, lang_code, pages, rating, pub_date, publisher):
        '''
        :param media_id: Media ID.
        :type: String
        :param title: Title of Media.
        :type: String
        :param authors: Author of Book.
        :type: String
        :param avg_rating: Rating of Book.
        :type: Float
        :param isbn: isbn of Book.
        :type: String
        :param isbn13: isbn13 of Book.
        :type: String
        :param lang_code: Language of Book.
        :type: String
        :param pages: Pages in Book.
        :type: Int
        :param rating: Rating count of Book.
        :type: Int
        :param pub_date: Publishing date of Book.
        :type: String
        :param publisher: Publisher of Book.
        :type: String
        '''
        super().__init__(media_id, title, avg_rating)
        self.__authors = authors
        self.__isbn = isbn
        self.__isbn13 = isbn13
        self.__lang_code = lang_code
        self.__pages = pages
        self.__rating = rating
        self.__pub_date = pub_date
        self.__publisher = publisher


    # All the Getter and Setter function for member variables.
    def get_authors(self):
        return self.__authors

    def set_authors(self, authors):
        self.__authors = authors

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn13(self):
        return self.__isbn13

    def set_isbn13(self, isbn13):
        self.__isbn13 = isbn13

    def get_lang_code(self):
        return self.__lang_code

    def set_lang_code(self, lang_code):
        self.__lang_code = lang_code

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        self.__pages = pages

    def get_num_ratings(self):
        return self.__rating

    def set_num_ratings(self, rating):
        self.__rating = rating

    def get_pub_date(self):
        return self.__pub_date

    def set_pub_date(self, pub_date):
        self.__pub_date = pub_date

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher):
        self.__publisher = publisher
