MyName = input("enter your name please  ")
MyAge = int(input("enter age please  "))

print(f"My name is {MyName} and I am {MyAge} years old")

No1 = int(input("Enter number  "))
No2 = int(input("Enter another number  "))
op = input("please choose an operation / * - +")
x = No1 * No2
d = No1/No2
p = No1 + No2
m = No1 - No2

if op == "/":
    print(f"{No1}/{No2} = {d}") 
elif op == "*":
    print(f"{No1}*{No2} = {x}")
elif op == "-":
    print(f"{No1}-{No2} = {m}")
elif op == "+":
    print(f"{No1}+{No2} = {p}")
else:
    print("what is wrong with u")

bus_capacity = 30
people_inbus = int(input("enter people boarding please  "))
empty_seats = bus_capacity - people_inbus

if empty_seats > people_inbus:
    print("there is room in the bus")
elif empty_seats == people_inbus:
    print("bus is full")
else:
    print("there is too many people kill them")