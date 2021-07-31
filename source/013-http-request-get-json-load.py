import requests

# pip install tabulate
from tabulate import tabulate

def showJsonData(data):

    items = {
        "hash":[],
        "time":[]
    };

    columns = ["Hash","Time"]
  

    for txs in data["txs"]:
        items["hash"].append(txs["hash"])
        items["time"].append(txs["time"])

    print(
        tabulate(
            items,
            headers = columns
        )
    )

def main():

        # BlockChain Info - unconfirmed transactions
        r =  requests.get("https://blockchain.info/unconfirmed-transactions?format=json")

        if(r.status_code == 200):
            showJsonData(r.json())
        else:
            print("ERROR from server" + str(r.status_code))

        exit()

if __name__ == "__main__":
    main()