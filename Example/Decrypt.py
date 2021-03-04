#First, we will import Crytocode
import cryptocode #if this shows error, type pip install cryptocode in the console


def with_variables():
    #password for our string
    password = "mypassword"

    #text to encode
    encrypted_text  = "H4ZNKr0F*6kiRydXO550rftyRQQCXhg==*jdR59rxV41HS2pycnHFq7Q==*49YFs7DL8Z1FA2Q+0wOA/A=="

    #encoding text
    encoded = cryptocode.decrypt(encrypted_text, password)
    
    #printing
    print(encoded)
    
def asking_for_pass_and_text():
    #asking for password for our string
    print("Please enter the password")
    password = input()

    #asking for text to encode
    print("Please enter the encrypted text")
    encrypted_text  = input()

    #encoding text
    encoded = cryptocode.decrypt(encrypted_text, password)
    
    #printing
    print(encoded)
    
asking_for_pass_and_text()
# with_variables()