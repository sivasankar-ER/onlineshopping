products = ["Laptop", "Phone", "Headphones", "Tablet", "Charger"]
prices = [75000, 25000, 2000, 40000, 500]

order = input("Enter 'asc' or 'desc': ")

if order == 'asc':
    prices.sort()
    print("Low to High:", prices)
else:
    prices.sort(reverse=True)
    print("High to Low:", prices)
