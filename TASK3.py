import random as r
import string as s

try:
    length = int(input("Enter the length of the password: "))
    
    if length <= 0:
        print("Password length must be greater than 0.")
    else:
        random_letters = s.ascii_lowercase + s.ascii_uppercase + s.digits + s.punctuation
        
        password = ''.join(r.choice(random_letters) for _ in range(length))
        print("Random password is:", password)

except ValueError:
    print("Invalid input! Please enter a valid integer.")