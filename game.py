import time
import sys
def delay_print(s):
    for char in s:
        print(char, end='')
        time.sleep(0.040)

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
     print("Hint: S for Start Game\n")
     print("      Q for Quit\n")
     input1 = input("input:")
     if input1 == "s":
         loop = 2
         print("hello")


