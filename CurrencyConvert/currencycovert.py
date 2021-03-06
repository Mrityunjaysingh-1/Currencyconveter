# CURRENCY CONVETER IN PYTHON

with open('E:\Python\CurrencyConvert\CurrencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter Amount:\n"))
print("Enter the name of currency you want to convert this amount to?\nAvailable Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these value:\n")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")