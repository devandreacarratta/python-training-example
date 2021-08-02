import os 

# pip install pandas
import pandas 

def main():

    baseFolder = os.path.dirname(
        os.path.realpath(__file__)
    )

    fullPath = baseFolder + "\datasource\surveys.csv"

    data = pandas.read_csv(
        fullPath,
        sep='|',
        header=1
    )
    
    print(data)

    exit()

if __name__ == "__main__":
    main()