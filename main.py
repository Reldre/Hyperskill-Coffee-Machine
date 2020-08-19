water = 400
milk = 540
beans = 120
cups = 9
money = 550
program = True

def status():
    print()
    print("The coffee machine has:")
    print(water, " of water")
    print(milk, " of milk")
    print(beans, " of coffee beans")
    print(cups, " of cups")
    print("$", money, " of money", sep="")
    print()
    
   
def take():
    global money
    print()
    print("I gave you $", money, sep="")
    money -= money
    print()
    
def fill():
    global water
    global milk
    global beans
    global cups
    print()
    print("Write how many ml of water do you want to add:")
    add_water = int(input())
    water += add_water
    print("Write how many ml of milk do you want to add:")
    add_milk = int(input())
    milk += add_milk
    print("Write how many grams of coffee beans do you want to add:")
    add_beans = int(input())
    beans += add_beans
    print("Write how many disposable cups of coffee do you want to add:")
    add_cups = int(input())
    cups += add_cups
    print()
    
def buy():
    global water
    global milk
    global beans
    global cups
    global money 
    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    request = input()
    if request == "1":
        if water >= 250 and beans >= 16 and cups >= 1:
            water -= 250
            beans -= 16
            cups -= 1
            money += 4
            print("I have enough resources, making you a coffee!")
            
        elif water < 250:
            print("Sorry, not enough water!")
        elif beans < 16:
            print("Sorry, not enough beans!")
        elif cups < 1:
            print("Sorry, not enough cups!")
            
        print()
            
    elif request == "2":
        if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money += 7
            print("I have enough resources, making you a coffee!")
            
        elif water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif beans < 20:
            print("Sorry, not enough beans!")
        elif cups < 1:
            print("Sorry, not enough cups!")
            
        print()
            
    elif request == "3":
        if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6
            print("I have enough resources, making you a coffee!")
            
        elif water < 200:
            print("Sorry, not enough water!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        elif beans < 12:
            print("Sorry, not enough beans!")
        elif cups < 1:
            print("Sorry, not enough cups!")
            
        print()
            
    elif request == "back":
        pass
        
    
while program == True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "exit":
        program = False
    elif action == "remaining":
        status()
    
