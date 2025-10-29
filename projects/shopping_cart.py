items=[]
prices=[]
total=0
count=0
try:
    while True:
            item=input("Enter a item (q for quit) : ")
            if item.lower()=="q":
                break
            else:
                price=float(input("enter the item price: "))
                items.append(item)
                prices.append(price)
                count=count+1
                    
    print()
    print("----- YOUR CART -----")
    print("items - price ")
    for x in range(0,count):
            print(f"{items[x]} - {prices[x]}") 
    for price in prices:
            total+=price
    print()
    print(f"Total is {total}")

except:
      print('invalid input')


