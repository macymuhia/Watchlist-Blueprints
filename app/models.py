class Movie:
    def __init__(self, id, title, overview, poster, rating, vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.rating = rating
        self.vote_count = vote_count


class Review:
    all_reviews = []

    def __init__(self, movie_id, title, image_url, review):
        self.movie_id = movie_id
        self.title = title
        self.image_url = image_url
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()


    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response
