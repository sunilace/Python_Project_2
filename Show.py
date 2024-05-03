from Media import Media

class Show(Media):
    def __init__(self, media_id, show_type, title, directors, actors, avg_rating, country_code, added_date, release_year, rating, duration, genres, description):
        super().__init__(media_id, title, avg_rating)
        self._show_type = show_type
        self._directors = directors
        self._actors = actors
        self._country_code = country_code
        self._added_date = added_date
        self._release_year = release_year
        self._rating = rating
        self._duration = duration
        self._genres = genres
        self._description = description

    def get_show_type(self):
        return self._show_type

    def set_show_type(self, show_type):
        self._show_type = show_type

    def get_directors(self):
        return self._directors

    def set_directors(self, directors):
        self._directors = directors

    def get_actors(self):
        return self._actors

    def set_actors(self, actors):
        self._actors = actors

    def get_country_code(self):
        return self._country_code

    def set_country_code(self, country_code):
        self._country_code = country_code

    def get_added_date(self):
        return self._added_date

    def set_added_date(self, added_date):
        self._added_date = added_date

    def get_release_year(self):
        return self._release_year

    def set_release_year(self, release_year):
        self._release_year = release_year

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        self._rating = rating

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def get_genres(self):
        return self._genres

    def set_genres(self, genres):
        self._genres = genres

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description
