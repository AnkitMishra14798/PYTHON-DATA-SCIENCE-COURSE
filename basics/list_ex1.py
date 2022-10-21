movies = ['sholay','DDLJ','Ironman','Sooryavansham','sooryavanshi',
          'RRR','Kung Fu Panda','Batman','Inception']

print(len(movies))
print(movies)

movies.sort()
print(movies)

movies.reverse()
print(movies)

print('first movie',movies[0])
print('last movie',movies[-1])
print('all movies except first 3',movies[3:])
print('movies with even intexes.',movies[::2])