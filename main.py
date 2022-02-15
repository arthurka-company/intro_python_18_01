n = int(input())
if (n == 0):
    print(1)
    exit()
countZero = 0
while (n % 10 == 0):
    n //= 10
    countZero += 1
print(countZero)