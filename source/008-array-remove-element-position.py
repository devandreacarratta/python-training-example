# python 008-array-remove-element-position.py

numbers =[
    10, # position 0 
    20, # position 1
    30, # position 2
    40  # position 3
]


def main():
    print(numbers)
    
    # Remove item / position 2
    numbers.pop(2)

    print(numbers)

if __name__ == "__main__":
    main()