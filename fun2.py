# def get_salary():
#  val = int(input("enter amt"))
#  fine = 0.9
#  sal = val * fine
#  return sal

# print(get_salary())

# ans = get_salary()

# print("salary",ans)


from curses.ascii import SI


def amount():
    p = int(input("Enter the value of p"))
    r = int(input("Enter the value of r"))
    t= int(input("Enter the value of t"))
    SI = (p * r * t) / 100 
    amt = SI + p
    return amt
    print(amount())

print(f'the Amount will be {amount} on simple interest {SI}')

# or this way

print(f'the Amount will be {amount()[0]}')


