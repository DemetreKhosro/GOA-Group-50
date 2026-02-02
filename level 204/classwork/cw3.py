# შექმენი კლასი Movie, რომელსაც ექნება: title, rating, year, შექმენი 3 ფილმი და დაბეჭდე მხოლოდ  ის ფილმები, რომელთა რეიტინგი 8-ზე მეტია.

class Movie:
  def __init__(self, title, rating, year):
    self.title = title
    self.rating = rating
    self.year = year

movie1 = Movie("breaking bad", 9.5, 2008)
movie2 = Movie("dexter resurrection", 7.5, 2025)
movie3 = Movie("interstellar", 8.7, 2014)

movies = [movie1, movie2, movie3]

for movie in movies:
  if movie.rating > 8:
    print(movie.title)