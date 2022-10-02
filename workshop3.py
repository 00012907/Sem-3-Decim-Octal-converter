#Decimal to Octal Sem3 Workshop;
decimal = int(input("Enter a decimal number: "))
print("The octal equivalent is: ", decimal_to_octal(decimal))
def decimal_to_octal(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10
        return octal



