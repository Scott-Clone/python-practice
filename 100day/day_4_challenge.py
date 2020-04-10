from collections import defaultdict, namedtuple, Counter, deque
import csv
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

# Define a named tuple with fields that we need

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data = movies_csv):
	"""Extracts all movies from csv an stores them in a dict.
	   where keys are directors, and values is a list of movies (names tuples)"""
	directors = defaultdict(list)
	with open(data) as f:
		for line in csv.DictReader(f):
			try:
				director = line['director_name']
				movie = line['movie_title'].replace('\xa0', '')
				year = int(line['title_year'])
				score = float(line['imdb_score'])
			except ValueError:
				continue

			m = Movie(title = movie, year = year, score = score)
			directors[director].append(m)
	return directors


directors = get_movies_by_director()

# Print out movies from a director 
print(directors['Christopher Nolan'])

# Count movies per director
cnt = Counter()
for director, movies in directors.items():
	cnt[director] += len(movies)

print(cnt.most_common(5))

