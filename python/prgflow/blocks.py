#for i in range(1, 13): 
#    print("No. {} squred is {} and cubed {:4}".format(i, i ** 2,i **3))
#    print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))
print(age)

if age>= 18:
    print("You are old enough to vote")
