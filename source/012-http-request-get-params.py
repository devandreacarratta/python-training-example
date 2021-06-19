# python 012-http-request-get-params.py

# pip install requests

import requests

def main():

    keyword = input("KeyWord to Search in google: ") 
    
    querystringvalues = {'q': keyword}

    r = requests.get("https://www.google.com/search",params=querystringvalues)

    print(r.text)
    print(r.url)

    print("Response StatusCode" , r.status_code)
    print("Response Headers" , r.headers)
    print("Response Content" , r.content)

    exit()

if __name__ == "__main__":
    main()