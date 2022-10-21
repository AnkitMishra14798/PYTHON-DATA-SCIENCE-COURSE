books = ['Steelheart','Twelveth Fail','Osmosis','Calamity','Firefight']

books.append('The Final Empire')
books.append('Atomic Habit')
books.append('You can win')
books.append('Three mistake of my life')

print('idx\t| books')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')


books[6] = 'The Well of Ascension'  #update : replace the first name
books[-1] = 'The Hero of Ages'
books[2] = 'Legion'


print('idx\t| books')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')


books.insert(3,'Legion: Skin deep')
books.insert(5,'Elantris')

print('idx\t| books')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')


books.remove('Steelheart')
books.remove('Legion')

print('idx\t| books')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

#Extend Function

fruits = ['Apple','Mango','Grapes','Banana','Cherry']
dry_fruits = ['Almond','Cashew','Walnet','Coc+onut']
fruits.extend(dry_fruits)
print(fruits)