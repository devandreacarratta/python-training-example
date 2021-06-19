# python 009-array-remove-element-value.py

numbers =[
    10, # position 0 
    20, # position 1
    30, # position 2
    40  # position 3
]


def main():
    print(numbers)
    
    # Remove item by value
    numbers.remove(20)

    print(numbers)

if __name__ == "__main__":
    main()