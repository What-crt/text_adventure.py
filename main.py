# MA AH EP DG 6th Final-text adventure

#Elias' part

base_buff = 0
use_super_buff = 2
buff = 1
current_buff = 0
apple = buff
bread = buff
cheese = -2 

#current_buff += buff

#current_buff += use_super_buff



base_hp = 3
hp = base_hp + current_buff
if current_buff == 0:
    print("")
elif current_buff < 0:
    if current_buff <= - 3:
        base_hp - 3
    elif current_buff == -2:
        base_hp - 2
    else:
        base_hp - 1

if base_hp <= 0 :
    print("You Lose... Want to play again?")
elif base_hp > 5:
    print ("You win!!!")
atk = 1
charge = 2


player_atk = 1
player_charge = 3

#Mykel's part
name = input("What is your name?")
print(f"Hello {name}! welcome to the tutorial for 'Text Adventure'! ")
print("When asked a question, you will awnser with your preferred option. These choices will influence your adventure.")
print("For Example:")
awnser = input("You see two shops. A weapon shop and food market. You only have enough money to buy one thing. Weapon = w and food = f.")
if awnser == "w":
    print("Nice! you bought yourself a new sword!")
else:
    if awnser == "f":
        print("yum! You bought a sack of apples!")
print(f"Nice choice {name}!")
print("Now that know how your adventure will work you are ready!")
print("When you were young, you heard myths of an ancient golden egg that provides vast healing capabilities. Now that you're finally old enough, you will begin the search for it, whether it's myth or not.")
print("Warning: If you make a wrong choice you could get seriously hurt or even be forced to restart.")
print("Good luck brave adventurer!")
print("------------")

#Ambar's part
awnser =input("You stumble across two paths, one is a bright path = b and the other a dark path = d. what path will you choose?")
if awnser == "d":
    print("You find a bakery! You buy a loaf of bread. Yum! you gain one Hp.")
    current_buff += buff
    print("You keep exploring and come across a weapon shop.")
else:
    if awnser == "b":
        print("You find a lesser bandit.")
        bandit= input("Fight or Run, Press 1 to fight, 2 to run.")
        if bandit == "1":
            print("You lose two Hp.")
            hp - charge
            print("You are at 1 hp. Consume food to regain health.")
            print("You stumble into a weapon shop.")
        else:
            if bandit == "2":
                print("You leave unharmed and come across a weapon shop.")

weapon_shop = input("You decide that having a weapon would be smart. Would you like a sword = s or a axe = x?")
if weapon_shop == "s":
    print("Your weapon of choice is a sword, good pick!")
    print("You come to a large jungle full of mystery.")
else:                          
     if weapon_shop == "x":
        print("Your weapon of choice is a axe, nice!")
        print("You come to a large jungle full of mystery.")

inventory = [f"modly cheese", "bread", "Your weapon"]

jungle = input("You see two walkways. Do you go left or right?")
if jungle == "left":
    print("You continue your journey.")
else:
    if jungle == "right":
        print("You walk of a cliff to your doom. D: Better luck next time.")
        hp = -10000000
    

inventory= ["moldy cheese", "bread", "Your weapon"] #Mykel helped with inentory


#Domininiks part
print("you find a jungle temple do you want to go inside?")
yesno = input("yes or no?")
          
if yesno == "yes": 
    print("you find a giant spider")

else:
    if yesno == "no":
        wolves = input("You keep walking and come upon a pack of wolves. What would you like to do? run= r or keep going = k.")
        if wolves == "r":
            print("You run from the wolves. They see you and start chasing you. The only safe place is the jungle temple, so you run inside.")
            print("Inside you only find more trouble. Standing infront of you is a giant spider.")
        else:
            if wolves == "k":
                print("You are sadley attacked and hurt. You are forced to find safety in the jungle temple.")
                print("As you limp inside you find a giant spider inside staring right at you.")


fightrun=input("Would you like to run again = r or fight the spider = f?")
if fightrun == "f":
    stab=input("stab= st or slash= sl?")
    
    if stab == 'st':
        print("The spider, now wounded, backs into its web.The spider gets tangled in its web and is struggling to get up. This gives you a chance to glance around the temple, lying on the floor is key.")
        spider = input("In the few minutes or even secounds you have what do you do? pick up the key = k or finish fighting the spider = s?")
        if spider == "k":
            print("You quickly grab the key. Luckily the spider is still tangled, so you scan the room again.")
            print("You see a small key hole ingraved into the rock flooring. You stick the key inside. Its a perfect fit!")
            print("you unlock it and go down a long dark hall, you squint your eyes and come across yet another gigantic spider and behind it you see the golden egg.")
            spider_2 = input("This might me the last chance to get the golden egg. Do you ask the spider for the egg = a or fight the spider = f?")
            if spider_2 == "a":
                 print("the spider picks you up and eats you alive. D: Better luck next time!")
                 hp = -10000000
            else:
                if spider_2 =='f':
                    inventoryask = input("Do you want to use a something from your inventory? yes or no?")            #Mykel helped with inventory
                    if inventoryask == 'yes':
                        print(f"you have {inventory} in your inventory.")
                        inventory_question = input("what would you like to use? if cheese= c, if bread = b, and if sword = s.")
                        if inventory_question == "s":
                            print("You fight the giant spider and stab it in the eye. It crumples to the ground.")
                            print("YOU WIN!!!!!!")
                            print(f"After so long you finally found the Golden Egg! NICE WORK {name}!")
                            print("---------")
                            print("That was awesome! if you want to play again then push the play button again! (: (: (:")
        else:
            if spider == "s":
                print(f"You swing your {weapon_shop} at the busy spider. Nice Shot! You defeat the spider! After taking a quick breather you pick up the key.")
                print("You see a small key hole ingraved into the rock flooring. You stick the key inside. Its a perfect fit!")
                print("you unlock it and go down a long dark hall, you squint your eyes and come across yet another gigantic spider and behind it you see the golden egg.")
                spider_3 = input("This might me the last chance to get the golden egg. Do you ask the spider for the egg = a or fight the spider = f?")
                if spider_3 == "a":
                         print("the spider picks you up and eats you alive. D: Better luck next time!")
                         hp = -1000000
                else:
                    if spider_3 =='f':
                        inventoryask = input("Do you want to use a something from your inventory? yes or no?")            #Mykel helped with inventory and some coding around it.
                        if inventoryask == 'yes':
                            print(f"you have {inventory} in your inventory.")
                            inventory_question = input("what would you like to use? if cheese= c, if bread = b, and if weapon = s.")
                            if inventory_question == "s":
                                    print("You fight the giant spider and stab it in the eye. It crumples to the ground.")
                                    print("YOU WIN!!!!!!")
                                    print(f"After so long you finally found the Golden Egg! NICE WORK {name}!")
                                    print("---------")
                                    print("That was awesome! if you want to play again then push the play button again! (: (: (:")

                            else:
                                if inventory_question == "c" or inventory_question == "b":
                                    print("You throw the food at the monster. It bounces off one of its many legs and it attacks. D: Better luck next time!")
                                    hp = -10000000
                                   
    else:                                
        if stab == 'sl':
                print("You ended up not hiting it as hard as you ment to and now the spider is mad.")
                print("The spider dosent give you another chance to fight and swallows you. D: Better luck next time!")
                hp = -10000000
else:
    if fightrun == "r":
        print("The spider begins to chase you. But since you are far slower then the spider catches you. D: Better luck next time!")
        hp = -10000000