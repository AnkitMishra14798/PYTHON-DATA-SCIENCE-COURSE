# 1- Create a String and print it =====>>

str = 'Hello Zaid Sir'
print(str)

# 2- Take a string input and print it's lenght====>>

str = 'Hello Zaid Sir'
print(str)
print('The lenght of str is : ',len(str))

# 3- Print the last word of string "Python is great" using slices ====>>

str = "Python is great"
print('The lenght of str is : ',len(str))
print(str[-5:])
print(str[9:15])
print(str[9:])

# 4- Print the each word in different line of string "Python is everywhere" ===>>

str = 'Python is everywhere'
print('idx\t | str')
for i,s in enumerate(str):
    print(f'{i}\t| {s}')

# second way of same thing ====>>

str = 'Python is everywhere'
print(*str.split(), sep='\n')

# 5- Print the string "Hello World!" in reverse ===>>

str = "Hello World"
print(str[::-1])

# 6- Convert the string "How are you?" in upper case ===>>

str = "How are you?"
print('uppercase =>> ',str.upper())

# 7- Convert the string "HOW IS IT GOING?" in upper case ===>>

str =  "HOW IS IT GOING?"
print('lowercase =>> ',str.lower())

# 8- Join the following list by spaces and print the result ===>>

words = ['Python', 'is', 'easy', 'to', 'learn']
print(*words)

# second way of same thing (without any spaces) ====>>

words = ['Python', 'is', 'easy', 'to', 'learn']
strlist = ''.join(words)
print(strlist)

# 9- print a multiline string using a single print ===>>

str = "If u want to do Industrial Trainning then... \n" "U should join the Digipodium classes... \n" "at Hajratganj \n."
print(str)

# 10- Print the string "to move to newline '\n'is used ."(result should look exactly like the provided string) ===>>

str = "If u want to do Industrial Trainning then... \n" "U should join the Digipodium classes... \n" "at Hajratganj \n."
print(str)

# 11- Print a variable with some text using a single print function, output should look like following.
#  the variable is 15  ===>>

a = 15
print('The variable is',(a))

# 12- Concatenate the following string and print the result ===>>

s1 = 'python'
s2 = 'is'
s3 = 'great.'
print(f'{s1} {s2} {s3}')
# or second type -------->>>>
s4 = s1 + s2 + s3
print(s4)
# or third type --------->>>>>
strlist = " ".join(s4)
print(s4)

# 13- Print '#' 20 times without using loop ===>> 

name = '#'
print((name + " ")*20)
# or second type -------->>>>
name = '#'
print(name * 20)

ques no14
for i in range(1,10):
    print(i,".")

#ques no 15
sentnce=input("enter the sentance : ")
print(*sentnce.split(),sep='\n')

#ques no 16
if sentnce[len(sentnce)-1]=='?':
    print("The entered strng has '?' in the end of the String")
else:
    print("The entered sentance does not have '?' in it. ")

#ques no 17
print(sentnce.count('e'))

#ques no 18
print(sentnce.isnumeric())

#ques no 19
text="    this is not a good String     "
sen=text.lstrip()
print(sen.rstrip())

#ques no 20
for i in sentnce:
    if i.isupper():
        print("Found")