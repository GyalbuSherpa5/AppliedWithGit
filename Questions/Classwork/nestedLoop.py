from datetime import date


def initalize():
    print(f"""
Sunway Int'l Business School
    Maitidevi, Kathmandu
                date: {date.today()} 
""")


initalize()


cus = int(input("Enter no. of customer: "))
cusDetail = []
cusItem = []
total = []


def getItem(num):
    cusSum = 0
    for j in range(num):
        unit = int(input(f"Enter Number of item [{j+1}] : "))
        price = int(input(f"Enter price of item [{j+1}] : "))
        print()

        totalPrice = unit * price
        cusSum += totalPrice

    total.append(cusSum)

    return cusSum


def inputInfo():
    for i in range(cus):

        cusNAPE = [input(f"Enter the id of customer [{i + 1}] : "), input(f"Enter the name of the customer [{i + 1}] : ")]
        cusDetail.append(cusNAPE)
        print()
        item = int(input("Enter the quantity of item : "))
        print()
        cusItem.append(getItem(item))


inputInfo()
# print(cusDetail)
# print(cusItem)

disAmount = []


def dis():
    for i in cusItem:
        if 5000 < i < 8000:
            discount = 0.05 * i
            disAmount.append(discount)
        elif 8000 < i < 10000:
            discount = 0.08 * i
            disAmount.append(discount)
        elif i > 10000:
            discount = 0.1 * i
            disAmount.append(discount)
        else:
            disAmount.append(0)


dis()
# print(disAmount)


def finalize():
    initalize()

    for k in range(cus):
        print(f"""

customer id : {cusDetail[k][0]}
customer name : {cusDetail[k][1]}
total price : {total[k]}
discount amt : {disAmount[k]}

""")


finalize()
