#First, we will import Crytocode
import cryptocode #if this shows error, type pip install cryptocode in the console


def with_variables():
    #password for our string
    password = "mypassword"

    #text to encode
    text  = "mytext"

    #encoding text
    encoded = cryptocode.encrypt(text, password)
    
    #printing
    print(encoded)
    
def asking_for_pass_and_text():
    #asking for password for our string
    print("Please enter the password")
    password = input()

    #asking for text to encode
    print("Please enter the text")
    text  = input()

    #encoding text
    encoded = cryptocode.encrypt(text, password)
    
    #printing
    print(encoded)
    
with_variables()
# asking_for_pass_and_text()