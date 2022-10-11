from tempfile import TemporaryDirectory

def is_armstrong_number(number):
    digCount = len(str(number))
    # print(digCount)
    tempNum = number
    sum = 0
    while tempNum > 0:
        tempSum = int(tempNum % 10)
        sum += tempSum**digCount
        tempNum = int(tempNum/10)
        # print(sum)
        # print(tempNum)
    if (number == sum):
        return True
    else:
        return False


print(is_armstrong_number(153))
