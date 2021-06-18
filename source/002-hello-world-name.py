# python 002-hello-world-name.py

def main():
    # Acquire name in 'name' 
    # Pay Attention - space in the end on input
    # Otherwise the 'input' will be after '?'
    name = input("What's your name? ")

    print("Hello World" , name,"!")

    exit()

if __name__ == "__main__":
    main()