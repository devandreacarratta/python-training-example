# python 003-array-loop-for.py

foods =[
    "Marinara",
    "Margherita",
    "Romana",
    "Quattro Formaggi",
    "Quattro Stagioni",
    "Diavola"
]


def main():
    print("Pizza & Pizza")

    index = 0

    while index < len(foods):
        print(
            index + 1,
            " - ",
            foods[index])

        index+=1;
 
    exit()

if __name__ == "__main__":
    main()