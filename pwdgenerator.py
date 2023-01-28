import random
import secrets
import string
all_digits=string.digits #having all digits
all_letters=string.ascii_letters # combining all letters in both uppercase or lowercase
all_symbols=string.punctuation # having all symbols
all_things=all_digits+all_letters+all_symbols #grouping all of them together digits, letters, and symbols
length=int(input('enter the length of password:')) #length of the password to be entered by the user
password=''
for i in range (length):
    password+=''.join(secrets.choice(all_things)) #creating a random password which is cryptographically secure
print(password)