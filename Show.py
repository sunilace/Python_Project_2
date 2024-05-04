# Author: Sunil Gupta, Sainithya Surasani, Nihal Reddy Akula.
# Date: 5/5/2024
# Description: Python Project 2 code.


from Media import Media

class Show(Media):
    # Constructer function.
    def __init__(self, media_id, show_type, title, directors, actors, avg_rating, country_code, added_date, release_year, rating, duration, genres, description):
        '''
        :param media_id:  To store Media ID.
        :type: String
        :param show_type: Type of show.
        :type: String
        :param title: To store media Title.
        :type: String
        :param directors: Director of show.
        :type: String
        :param actors: Actors involved in the show.
        :type: String
        :param avg_rating: Rating for media.
        :type: Float
        :param country_code: Country.
        :type: String
        :param added_date: Date added.
        :type: String
        :param release_year: Release year of the movie.
        :type: Int
        :param rating: Rating count of show.
        :type: String
        :param duration: Duration of movie.
        :type: String
        :param genres: Genres of the show.
        :type: String
        :param description: Description of the show.
        :type: String
        '''
        super().__init__(media_id, title, avg_rating)
        self.__show_type = show_type
        self.__directors = directors
        self.__actors = actors
        self.__country_code = country_code
        self.__added_date = added_date
        self.__release_year = release_year
        self.__rating = rating
        self.__duration = duration
        self.__genres = genres
        self.__description = description

    # All the getter and setter function for member variables.
    def get_show_type(self):
        return self.__show_type

    def set_show_type(self, show_type):
        self.__show_type = show_type

    def get_directors(self):
        return self.__directors

    def set_directors(self, directors):
        self.__directors = directors

    def get_actors(self):
        return self.__actors

    def set_actors(self, actors):
        self.__actors = actors

    def get_country_code(self):
        return self.__country_code

    def set_country_code(self, country_code):
        self.__country_code = country_code

    def get_added_date(self):
        return self.__added_date

    def set_added_date(self, added_date):
        self.__added_date = added_date

    def get_release_year(self):
        return self.__release_year

    def set_release_year(self, release_year):
        self.__release_year = release_year

    def get_rating(self):
        if self.__rating == "":
            return "None"
        else:
            return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_genres(self):
        return self.__genres

    def set_genres(self, genres):
        self.__genres = genres

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description
