import random

def passwordLen():

    message="Password Lenght: "

    while True:
        try:
            result = int(
                input(message)
            )       
        except ValueError:
            print("Input is not valid! Only number")
            continue
        else:
            return result 
            break 

def main():
    
    passwordLenght = passwordLen()

    chars = []

    for i in range(26):   
        # UpperCase  
        chars.append( chr(65 + i) )
         # LowerCase
        chars.append( chr(97 + i) )

    for i in range(10):
        # Number
        chars.append( chr(48 + i) )

    for i in range(16):
        # Special Chars 1
        chars.append( chr(32 + i) )

    for i in range(7):
        # Special Chars 2
        chars.append( chr(58 + i) )

    for i in range(6):
        # Special Chars 3
        chars.append( chr(91 + i) )

    for i in range(4):
        # Special Chars 4
        chars.append( chr(123 + i) )

    random.shuffle(chars)

    randomPassword  = "".join(chars)

    randomPassword = randomPassword[0:passwordLenght]
   
    print(randomPassword)

    exit()

if __name__ == "__main__":
    main()