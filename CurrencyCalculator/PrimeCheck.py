def primeCheck(number):
    if number == 1 or number == 2:
        return True
    for i in range(2, (number-1)):
        result=(number%i)
        if result == 0:
            return False
        else:
            return True
print (primeCheck(5))