#Grocery Store
'''
The program evaluates the total bill price and the discount price of the bill
according to the membership grade. The product price and buying list are both
presented in dictionary format. Then we create two functions that read the
dictionaries to get the bill price and the discount price.
'''

def get_price(product, quantity):
    sub_total = price_dic[product] * quantity
    print(product + ": $ " + str(price_dic[product]) + " x " + str(quantity) + " = " +\
         str(sub_total))
    return sub_total

def get_discount(bill_price, membership):
    discount = 0
    if bill_price >= 25:
        if membership == "gold":
            bill_price = bill_price * 0.75
            discount = 25
        elif membership == "silver":
            bill_price = bill_price * 0.85
            discount = 15
        elif membership == "bronze":
            bill_price = bill_price * 0.95
            discount = 5
        print(str(discount) + "% off for " + membership + \
            " membership at total price no less than $25")
    return bill_price

buying_dic = {"biscuit": 2, "chicken": 5, "egg": 20}
price_dic = {"biscuit": 2, "fish": 3, "chicken": 5, "cabbage": 2, "egg": 0.2}
bill_price = 0

for key, value in buying_dic.items():
    bill_price += get_price(key, value)
 
membership = "gold"

bill_price = get_discount(bill_price,membership)
print("The total price is $" + str(bill_price))