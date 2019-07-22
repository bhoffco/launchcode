how_many = float(input("how many donuts would your like? "))
how_much = float(input("how much would you like to pay? "))
tax = float(1.07)

cost = how_many * how_much * tax

print("After tax, your total is ${}.".format(round(cost, 2)))
