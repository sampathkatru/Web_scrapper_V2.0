import requests
from bs4 import BeautifulSoup as Bs
import pandas as pd
from time import sleep

product_name=[]
product_price=[]
product_rating=[]
product_description=[]

url="https://www.flipkart.com/search?q=television+55+inch&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&suggestionId=television+55+inch%7CTelevisions&requestId=662baa24-6ed5-4fcc-85d2-6685f07645e0&as-searchtext=telev&page="


for i in range(1,5):
    url="https://www.flipkart.com/search?q=television+55+inch&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&as-pos=2&as-type=RECENT&suggestionId=television+55+inch%7CTelevisions&requestId=662baa24-6ed5-4fcc-85d2-6685f07645e0&as-searchtext=telev&page=" +str(i)
    r=requests.get(url)
    print(r)
    soup=Bs(r.text,"lxml")
    cube=soup.find("div",class_="DOjaWF gdgoEp")
    name=cube.find_all("div",class_="KzDlHZ")
    for i in name:
        n=i.text
        product_name.append(n)
    print(len(product_name))
    price=cube.find_all("div",class_="Nx9bqj _4b5DiR")
    for i in price:
        n=i.text
        product_price.append(n)
    print(len(product_price))
    rating=cube.find_all("div",class_="XQDdHH")
    for i in rating:
        if i:
            n=i.text
            product_rating.append(n)
        else:
            product_rating.append("NIL")
    print(len(product_rating))

    desc=cube.find_all("ul",class_="G4BRas")
    for i in desc:
        n=i.text
        product_description.append(n)
    print(len(product_description))
    sleep(5)
 
        

print(len(product_name))
print(len(product_price))
#print(len(product_rating))
print(len(product_description))

df = pd.DataFrame({
    'Product Name': product_name,
    'Price': product_price,
   # 'Rating': product_rating,
    'Description': product_description
})



print(df.head())

# Save the DataFrame to a CSV file
df.to_csv('flipkart_televisions.csv', index=False)

