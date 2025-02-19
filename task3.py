#simple check using < and >
def checkNum(num):
    if num > 0:
        return "Pos num"
    elif num < 0:
        return "Neg num"
    else:
        return "Num is 0"

#loop for all nums until we get the first 10 prime nums
def firstTenPrimes():
    primes = []
    num = 2
    while len(primes) < 10:
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
        if isPrime:
            primes.append(num)
        num += 1
    return primes


#add all nums to 100 to a total
def sumNums():
    total = 0
    num = 1
    while num <= 100:
        total += num
        num += 1
    return total