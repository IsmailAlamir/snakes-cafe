menu ='''
**************************************
** Welcome to the Snakes Cafe!      **
** Please see our menu below.       **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
 
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
'''

list_menu=[
    "Wings",
    "Cookies",
    "Spring Rolls", 
    "Salmon",
    "Steak",
    "Meat Tornado",
    "A Literal Garden",
    "Ice Cream",
    "Cake",
    "Pie",
    "Coffee",
    "Tea",
    "Unicorn Tears"
]

print(menu)
order=input(">")
ss=[]

while order !="quit":
    if order in list_menu :
        ss.append(order)
        count = ss.count(order)
        print(f"** {count} order of {order} have been added to your meal **")
        order=input(">")

    else :
        print("please select from the menu")
        order=input(">")
if ss==[]:
    print ("** You didn't order anything **")
else: 
    print (f"** your meal is : **")
    summary=list(set(ss))
    for order in summary  :
        print (f"** {ss.count(order)} order of {order} **")


