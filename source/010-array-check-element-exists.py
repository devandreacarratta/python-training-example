# python 010-array-check-element-exists.py

numbers =[
    10, # position 0 
    20, # position 1
    30, # position 2
    40  # position 3
]


def main():
    
    
    find = 20 in numbers

    print(20,find)

    find = 0 in numbers

    print(0, find)


if __name__ == "__main__":
    main()