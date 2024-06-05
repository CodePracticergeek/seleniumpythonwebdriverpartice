
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


def reverseNuum():
    number = int(input("Enter the number"))
    reversenum = 0
    number_str = str(number)
    for digit in number_str:
        digit = number%10
        reversenum = int(digit)+ reversenum*10
        number//=10
    return reversenum



# print(reverseNuum())

original_Sring ="Hello World"
reverse_string = original_Sring[::-1]
print(reverse_string)




