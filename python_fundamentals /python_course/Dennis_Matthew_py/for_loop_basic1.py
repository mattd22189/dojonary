# Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000.
for i in range(5,101,5):
    print(i)
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,100,5):
    if i == 1%5:
        print("Coding")
    else:
        print(i)
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
for i in range(500000,0,2):
    print(i%1)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018,0,2):
    print(i%2)
#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
    
    """
    
    if i <= 5:
    i = low_num
elif i >= 5:
    i = high_num
for i in range(low_num,high_num,mult):
    
    """
