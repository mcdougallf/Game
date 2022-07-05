import time
import sys
import random
def delay_print(s):
    for char in s:
        print(char, end='')
        time.sleep(0.030)

#Import time Code used to delay printing keys
        
CHAINSAW_LIST = ['Front Handle\n', 'Chain Brake\n' , 'Guide Bar\n', 'Chain\n', 'Throttle\n', 'Engine\n']

SNIPER_LIST = ['Scope\n','Bolt\n','Barrel\n','Body\n','Trigger\n','Magazine\n']

#Constants (sniper and chainsaw list for house items)

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
#delay_print connects to the import time code
            
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

        
        
        street_list = ['Wykeham Hollies', 'Chester Green', 'Salisbury Yard', 'Lynmouth Park', 'Whitehouse Maltings', 'Beckett Laurels']
        
        sample_list = random.sample(street_list, 3)
        print(sample_list)
        street=input("Pick a Street: ") 
        street.lower()
        
#Import random code
    if street == 'Wykeham Hollies' or'Chester Green' or'Salisbury Yard' or'Lynmouth Park' or'Whitehouse Maltings' or'Beckett Laurels':
        
        delay_print("OK then\n")
        delay_print("Off you pop")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("Which House Would you Like to Raid?")
        delay_print("\n")
        delay_print("\n")

        

    letterbox_list = ['33', '34', '35', '36', '67', '69']

    sample_list = random.sample(letterbox_list, 4)
    print(sample_list)
    letterbox=input("Pick a House:  ")


    if letterbox in '33 36 68':

        delay_print("Raid Successful\n") 
        delay_print("You Found......\n")

        

        

        sample_list = random.sample(CHAINSAW_LIST, 2)
        delay_print(sample_list)
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("These parts are used to make a Chainsaw\n")
        delay_print("\n")
        delay_print("Press Enter to Continue\n")

        
# if and elif is to determine which weapon you chose (and what house you want to raid)                                     

    elif letterbox in '34 35 69':


        delay_print("Raid Successful\n")
        delay_print("You Found......\n")

        

        

        sample_list = random.sample(SNIPER_LIST, 2)
        delay_print(sample_list)
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("These parts are used to make a Sniper\n")
        delay_print("\n")
        delay_print("Press Enter to Continue\n")

x = input()
if x == "":

        delay_print("Ok Then\n")
        delay_print("Next House\n")
        delay_print("\n")
        delay_print("Press Enter to Continue\n")

x = input()
if x == "":

        

    letterbox2_list = ['72', '73', '74', '78', '80', '82']

    sample_list = random.sample(letterbox2_list, 4)
    print(sample_list)
    letterbox2=input("Pick another House:  ")

    if letterbox2 in '72 74 80':

        delay_print("Raid Successful\n")
        delay_print("You Found......\n")

        

        sample_list = random.sample(chainsaw_list, 2)
        delay_print(sample_list)
        delay_print("\n")
        delay_print("\n")
        delay_print("\n")
        delay_print("These parts are used to make a Chainsaw\n")
        delay_print("\n")
        delay_print("Press Enter to Continue\n")

x = input()
if x == "":

        delay_print("Next House")
    

        
