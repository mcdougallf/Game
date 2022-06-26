import time
import sys
def delay_print(s):
    for char in s:
        print(char, end='')
        time.sleep(0.030)

#Code used to delay printing of keys

delay_print("Press Enter To Start\n")
x = input()
if x == "":
    loop = 1
    while loop == 1:
        delay_print("Start Game\n")
        delay_print("\n")
        delay_print("Quit\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        print("Hint: s for Start Game\n")
        print("      q for Quit\n")
        input1 = input("input:")
        if input1 == "s":
            loop = 2
        elif input1 == "q":
            quit()
#Code for starting or quiting game
        delay_print("\n")
        delay_print("\n")    
        delay_print("Okay you see that man behind that house? ")
        delay_print("NO!? ")
        delay_print("Don't care,\n")
        delay_print("anyways go find a weapon and kill that man cause im not bothered getting my hands dirty")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("Which street do you want to begin your search?")
        delay_print("\n")
        delay_print("\n")

        import random
        
        street_list = ['Wykeham Hollies', 'Chester Green', 'Salisbury Yard', 'Lynmouth Park', 'Whitehouse Maltings', 'Beckett Laurels']
        
        sample_list = random.sample(street_list, 3)
        print(sample_list)
        street=input("pick a street: ") 
        
#Import random code

           
