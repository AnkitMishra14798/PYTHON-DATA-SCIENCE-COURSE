
data = read('pride_n_prejudice.txt')
from string import ascii_lowercase

for letter in ascii_lowercase:
    Counter = data.count(letter)
    print(f'{letter} found {Counter} times')