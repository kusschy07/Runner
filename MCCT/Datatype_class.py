##Number system coversion in python

num1 = 12345

#Decimal to Binary
print(bin(num1))
print(f"{bin(num1)}")

#Hexa-decimal conversion
print(hex(num1))
print(f"{hex(num1)}")

#0ctal conversion
print(oct(num1))
print(f"{oct(num1)}")

# _________________________________________________________________________________________
num2 = "11011"
output=int(num2)

print(output)

print(f"{int(num2,2)}")
print(f"{hex(int(num2,2))}")

"""Note:string can be change in integer as well int-->str,but can only int -->octal,hex,binary"""

# ________________________________________________________________________________________

# Hexa-decimal into binary,Decimal,octal

num3 ="FAA"

print(f"{bin(int(num3,16))}")
print(f"{(int(num3,16))}")
print(f"{hex(int(num3,16))}")
# ----------------------------------------------
num4= input("Enter your number :")

print(f"Binary={bin(int(num4,8))}")
print(f"Decimal={int(num4,8)}")
print(f"Hexa-Decimal2={hex(int(num4,8))}")


num5 = "2345"
output = int(num5)

print(f"Hexa_decimal={hex(int(num5))}")


 



