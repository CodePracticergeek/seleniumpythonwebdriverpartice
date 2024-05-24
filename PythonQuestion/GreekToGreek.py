
def amstrong_number():
    number = int(input("Enter the Number"))
    length = len(str(number))
    amstrong_number = 0

    while number!=0:
        reminder = number%10
        amstrong_number += reminder**length
        number = number//10
        print(number)

    if number == amstrong_number:
        print("Number is Amstrong", amstrong_number)
    else:
        print("Number is not amstrong", amstrong_number)


def prime_number():
    number = int(input("Enter the number"))
    while number!=0:
        if number//number==0 & number%2==1:
            print("Is a prime number")
        else:
            print("Is not a prime number")








