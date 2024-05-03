class Media:
    def __init__(self, media_id, title, avg_rating):
        self._id = media_id
        self._title = title
        self._avg_rating = avg_rating


    def get_id(self):
        return self._id

    def set_id(self, media_id):
        self._id = media_id

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_avg_rating(self):
        return self._avg_rating

    def set_avg_rating(self, avg_rating):
        self._avg_rating = avg_rating
