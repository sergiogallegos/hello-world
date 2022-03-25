string1 = "he's "
string2 = "probably "
string3 = "pinging "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

print("he's " "probably " "pinging " "for the " "fjords")

print("Hello " * 5)
print("Hello " * (5+4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)        # True
print("fri" in today)        # True
print("thur" in today)       # False
print("parrot" in "fjord")   # False


print("put your name: ")
a = input() 
print("put yor age :")
b = input()
print(a + b)
