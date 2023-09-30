#Answer (1-6)
Name = input("Enter your name")
Age = input("Enter your age")
Street = input("Enter your street")
City = input("Enter your city")
Country = input("Enter your country")
print(f'"Name:{Name}')
print(f'"Age:{Age}')
New_Age= int(Age)-5
print(f'"Adress:{Street}, {City}, {Country}')
print(f'"Hello{Name}, Your Age is{New_Age} years old, Your address is {Street}, {City}, {Country}')
print(type(Name), type (Age), type (Street), type (City), type(Country))
print(f'"Hello {Name},How Are You ? \\"Your age is"{New_Age}"+ And Your Countre is : {Country}')
print(f'''Hello'{Name}',How Are You ? \\
\\"Your age is"{New_Age}"+And
Your City is :{City}''')
#Answer (7-8)
Name= "ITF GSG python"
print(Name[0])
print(Name[2])
print(Name[-1])
print(Name[-3:])
print(Name[0:3])
print(Name[0:7:2])
print(Name[-1:-7:-1])
#Answer9
Name= "$&$Mohammed$&$&"
print(Name.strip("$&"))
#Answer10
Msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(Msg.replace("%7", "Love"))
#Answer11
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))
#Answer13
#Title converts the first letter of each words to uppercase
eg="hello ahmed"
print(eg.title())
#Capital converts the first letter of the first word to capital letter
ex="hello ahmed"
print(ex.capitalize())
#Answer14
first_name = "Dana"
print('*****'+first_name)
print('****'+first_name+'****')
print(first_name+'*****')
#Answer15
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
#Answer17
print(name_one.islower)
print(name_two.isupper)
