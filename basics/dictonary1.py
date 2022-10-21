# dictonary with integer key

my_dict = {1:'apple',2:'ball'}
print(my_dict)

val = ['Rajendra Singh', 30, 10, 'Account','Staff Officer',600000,7,]

val_dict = {
    'employee': 'Rajendra Singh', 'age': 30,
    'experience':10,'dept':'Account',
    'designation': 'System Officer', 'salary':600000,
    'team_size': 7
}

# display a dict
print(val_dict)

# retreival of value

ans = val_dict['designation'] # key in sqrbrackets
print(ans)
print(val_dict['salary'])   #corect
print(val_dict['experience'])  #incorect

# adding a data inside dict 
val_dict['comany'] = 'Acme.inc'

print(val_dict)

from pprint import pp

pp(val_dict)
