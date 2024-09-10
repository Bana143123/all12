import requests

def Exchange(api_key,our_currency,Target_currency):
    API_URL=f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{our_currency}/{Target_currency}"
    print(API_URL)
    response=requests.get(API_URL)
    data=response.json()
    #print(data)
    print(response.status_code)
    print(response.text)
    if response.status_code!=200:
        print("There is a issue with API_URL or api_key or currency Kindly cross check")
    return data


def converting(amount,money):
    Aftercon=money*amount
    return Aftercon
    




def main():
    api_key="d6c34968c04d1dde7c384a3a"
    print("Welcome To Currency Exchange ")
    our_currency=input("Enter the currency :").upper()
    Target_currency=input("Enter the targeted currency :").upper()
    money=float(input("Enter the amount here : "))
    EX_rate=Exchange(api_key,our_currency,Target_currency)
    amount=EX_rate["conversion_rate"]
    Final=converting(amount,money)
    print()
    print(f"Currency converting from {our_currency} to {Target_currency} is : {Final}")
    print()



if __name__=="__main__":
    main()