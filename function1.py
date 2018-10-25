def leapyear(Y):
    if(Y%4)==0:
        return True
    elif(Y%100)==0:
        return False
    elif(Y%400)==0:
        return True
    else:
        return False
Y=int(input("Enter a year: "))
print (leapyear(Y))
