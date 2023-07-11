# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# for i in range(0,6)[::-1]:
#     print(i)
    
#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# print_and_return = [4,5]
# def my_function():
#     for i in range(0, len(print_and_return)):
#         if i == print_and_return[0]:
#             print(i,print_and_return[0])
#         else :  
#             return print_and_return[1]
#         my_function()
#         print(my_function())
        
# #First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# my_list = [5,2,3,4,5,6,7,8,9]
# for i in range(0,len(my_list)):
#     print(my_list[0]+ i)

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
old_list = [22,45,78,-21,2,3,6]
new_list = []
def Value():
    for int in range(0,len(old_list)):
        if int > 6:
            new_list.append(i)
    print(new_list)
    Value()