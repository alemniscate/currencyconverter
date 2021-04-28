import requests
import json

dic = {}

sale_currency = input().lower()

r = requests.get("http://www.floatrates.com/daily/" + sale_currency + ".json")
d = json.loads(r.text)
if sale_currency.lower() != "usd":
    dic["usd"] = d["usd"]["rate"]
if sale_currency.lower():
    dic["eur"] = d["eur"]["rate"]

while True:
    buy_currency = input().lower()
    if buy_currency == "":
        break
    amount = float(input())

    print("Checking the cache...")
    if buy_currency in dic:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        r = requests.get("http://www.floatrates.com/daily/" + sale_currency + ".json")
        d = json.loads(r.text)
        dic[buy_currency] = d[buy_currency]["rate"]
    print("You received", round(dic[buy_currency] * amount, 2), buy_currency.upper() + ".")
