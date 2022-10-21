import email


email = input("Enter yor email")
if '@' in email and len(email) >= 11 and ('.com' in email or 'org' in email):
    print('this is right email')
else:
    print('sorry this is not email id')