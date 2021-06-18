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

    index=0

    for x in foods:
        index+=1;
        print(index," - ",x)
    

if __name__ == "__main__":
    main()