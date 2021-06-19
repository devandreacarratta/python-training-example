# python 006-array-add-elements.py

numbers =[
    1,
    2,
    3
]


def main():
    print(numbers)
    numbers.extend([4,5,6])
    print(numbers)

if __name__ == "__main__":
    main()