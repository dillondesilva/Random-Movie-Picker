import random 

movie = raw_input("Movie Option: ")
movies = []

while movie:
  movies.append(movie)
  movie = raw_input("Movie Option: ")

choice = random.choice (movies)
print "Random movie selector says to watch", choice
