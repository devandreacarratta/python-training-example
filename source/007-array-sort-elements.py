# python 006-array-add-elements.py

numbers =[
    6,
    1,
    3,
    2,
    4
]


def main():
    print(numbers)
    
    # Sort ASC
    numbers.sort()
    print(numbers)
    
    # Sort DESC
    numbers.sort(reverse=True) 
    print(numbers)

if __name__ == "__main__":
    main()