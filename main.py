# MA AH EP DG 6th Final-text adventure

#Elias' part

base_buff = 0
use_super_buff = 2
buff = 1
current_buff = 0
apple = 


#current_buff += buff

#current_buff += use_super_buff



base_hp = 3
hp = base_hp + current_buff
if current_buff == 0:
    print("You have run out of buff")
elif hp < 0:
    if hp <= - 3:
        base_hp - 3
    elif hp == -2:
        base_hp - 2
    else:
        base_hp - 1

if base_hp <= 0 :
    print("You Lose... Wanna play again?")
elif base_hp > 5:
    print ("You win!!!")
atk = 1
charge = 2


player_atk = 1
player_charge = 3

#Mykel's part
name = input("What is your name?")
print(f"Hello {name}! welcome to the tutorial for 'Text Adventure'! ")
print("When asked a question, you will awnser with your perferded option. These choices will influence your adventure.")
print("For Exaple:")
answer = input("You see two shops. A weapon shop and food market. You only have enough money to buy one thing. Weapon = w and food = f.")
if answer == "w":
    print("Nice! you bought yourself a new sword!")
else:
    if answer == "f":
        print("yum! You bought a sack of apples!")
print(f"Nice choice {name}!")
print("Now that know how your adventure will work you are ready!")
print("When you were young, you heard myths of an ancient golden egg that provides vast healing capabilities. Now that you're finally old enough, you will begin the search for it, whether it's myth or not.")
print("Warning: You have been given three lives. If you lose all three you will be forced to restart.")
print("Good luck brave adventurer!")

#Ambar's part
answer =input("You stumble across two paths, one is a bright path and the other a dark path. What path will you choose? ")
if answer == "bright path":
    print("You find a bakery! You buy a loaf of bread. Yum! you gain one Hp.")
    current_buff += buff
    print("You keep exploring and come across a weapon shop.")
else:
    if answer == "dark Path":
        print("You meet with a lesser bandit.")
        bandit= input("Fight or Run, Press 1 to fight, 2 to run")
        if bandit == 1:
            print("You lose two Hp.")
            print("You stumble into a weapon shop.")
        else:
            if bandit == 2:
                print("You leave unharmed and come to a weapon shop.")

weapon_shop = input("You decide that having a weapon



jungle = input("You see two walkways. Do you go left or right?")
if answer == "left":
    print("You continue your journey.")
    print("You find a Jungle temple.")
else:
    if jungle == "right":
        print("You fall in a hole and die D: you only have two lives left.")
    




#Domininiks part
print("you find a jungle temple do you want to go around")
yesno= input("yes or no ")
          
if yesno == "yes": 
    print("you find a giant spider")

    
    fightrun=input("run or fight")
    if fightrun == "fight":
        stab=input("stab or slash")
        stab=="stab"
        if stab == 'stab':
             print("The spider, wounded backs into its web to see another day and amidst the temple you see a key on the ground\n")
             key = print("you go inside the temple and see a key hole on the ground")
             if key == 'unlock':
                   print("you unlock it and you go down a hall and see a gigantic spider behind it you see the golden egg")
                   ask=print('do you ask or fight')
                   if ask=='ask':
                         print("she picks you up and you die")

        if stab == 'slash':
              print('you made the spider mad')
            hp - charge
    elif fightrun =="run":
               print("The spider begins to chase. But since you are far slower than the spider she catches you and peirces your body with a burning venom.")

else:
    print("you walk off of a cliff and fall to your doom")

