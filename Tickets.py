def calc_fee( n ):
    if n<=5:
        return n*100
    if n<= 10:
        return n*95
    else:
        return n*90



a= int(input("Please enter how many ticket you want"))
print ("you should pay {}".format(calc_fee(a)))
