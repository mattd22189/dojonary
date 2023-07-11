num1 = 42       #integer 
num2 = 2.3      #float
boolean = True      #boolean true or false
string = 'Hello World' #string literal
# list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# tuples
fruit = ('blueberry', 'strawberry', 'banana')
# output with type function
print(type(fruit))
# output with defining dictionary to print sausage topping 
print(pizza_toppings[1])
# .append() adds item to the end of a given list. 
pizza_toppings.append('Mushrooms')
# prints the name item in the dictionary
print(person['name'])
# changes the name item in the dictionary
person['name'] = 'George'
# adds an item to the dictionary called eye color and assigning it the color blue as a value. 
person['eye_color'] = 'blue'
# printing the fruit called banana to the console 
print(fruit[2])
# if statement checking if the variable is greater than 45 
if num1 > 45:
    print("It's greater")# printing its greater if the condition is true 
else:
    print("It's lower")# printing its lower if the condition is false 
#checking if the condition of a string variable is less than 5 characters 
if len(string) < 5:
    print("It's a short word!") #printing its a short word if the condition is true. 
elif len(string) > 15: #else checking if the string condition is greater than 15 characters
    print("It's a long word!")# printing to the console It's a long word! if the condition is true 
else:
    print("Just right!") # or else printing just right if neither the first nor second condition is true 
# for statement that counts the numbers of the integer adding it up from 0 to the set value 5 and printing the variable to the console each time 
for x in range(5): 
    print(x)
for x in range(2,5):#counting the numbers between 2 and 5 and printing the x variable to the console each time. 
    print(x)
for x in range(2,10,3):# counting the numbers between 2 and 10 and incrementing by 3 every time. 
    print(x)
x = 0 # assigning the value of x to 0 
# while statement that checks the condition of x and seeing if it is less than 5, then printing x
while(x < 5): 
    print(x)
    x += 1 # this is adding two values together and assigning the given value to x 

pizza_toppings.pop() #pop removing the last element in the list called pizza_toppings in this case it is removing olives from the list
pizza_toppings.pop(1) # pop removing the # 1 item from the list in this case it is removing sausages from the list variable called pizza_toppings

print(person) # printing the dictionary called person 
person.pop('eye_color') # popping and removing the eye_color variable from the person dictionary 
print(person)
# using a for loop to search through the pizza_toppings list and checking if the new variable called topping is equal to pepperoni in the dictionary.
for topping in pizza_toppings: 
    if topping == 'Pepperoni': # if the condition is true it is printing to the console 'After 1st if statement'
        continue
    print('After 1st if statement')
    if topping == 'Olives': # checking if the topping is equal to olives and breaking if the condition is true 
        break
# defining the the function of print_hello_ten_times()
def print_hello_ten_times():
    for num in range(10): # checking if the number is in the range of 10 
        print('Hello') #printing hello for every time the statement is run 

print_hello_ten_times() # calling the function 

def print_hello_x_times(x): #defining the function of print_hello_x_times(x) setting the parameters of the function 
    for num in range(x): # setting the range to the variable in the parameter 
        print('Hello')# printing hello every time the statement id run 

print_hello_x_times(4) # setting the argument as 4 saying it wants to run the function 4 times giving the argument to the parameter

def print_hello_x_or_ten_times(x = 10): #defining the function print_hello_x_or_ten_times(x = 10) saying to
    for num in range(x): # setting the range of the function as the variable x 
        print('Hello') # printing hello world every time the function is called 

print_hello_x_or_ten_times() # running the function as the default amount of times 
print_hello_x_or_ten_times(4) # setting the argument to 4.


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)