# python 011-http-request-get.py

# pip install requests

import requests

def main():

    # ex: https://jsonplaceholder.typicode.com/users
    url = input("Add url to GET: ") 
    
    r = requests.get(url)

    print("Response StatusCode" , r.status_code)
    print("Response Headers" , r.headers)
    print("Response Content" , r.content)

    exit()

if __name__ == "__main__":
    main()