import tkinter
import random
LossHP = 1
Game = tkinter.Tk()
Money = 15000
Max_HP = 100
HP = 100
Leather = 0
Apple = 0
Bread = 0
TMeat = 0
Meat = 0
Ale = 0
Wood = 0
watrP = 0
Water = 0
Sword = 0
Sheild = 0
ChainM = 0
Attack = 5
Armour = 0
Inv = Leather + Apple + Bread + Meat + Ale + Wood
Tinv = TMeat + Ale
CraftPower = 4
SleepHeal = 1
temp="Sleep, restore", SleepHeal,"HP"
STATS = "Gold: ",Money,", Max HP: ",Max_HP,", HP: ",HP,", Leather: ",Leather,", Apple: ",Apple,", Bread: ",Bread,", Meat: ",Meat,", Wood: ",Wood,", Water pouches: ",watrP,", water: ",Water,", Attack damage: ",Attack,", Defence: ",Armour,", Inventory space left: ",30 - Inv
print("Welcome to Village Life v.A1.0!")
print("The game is still in development, but so far you can do basic things like eat, buy things and craft.")
print("Enjoy!")
State = 1

def Leave(event):
    global State
    State = 1
    DestroyAllS()
    DestroyAllM()
    AddPlaces()

def AddHouses():
    House1.pack(padx=10, pady=10)
    House2.pack(padx=10, pady=10)
    House3.pack(padx=10, pady=10)
    House4.pack(padx=10, pady=10)

def AddPlaces():
    shop.pack(padx=10, pady=10)
    tavern.pack(padx=10, pady=10)
    well.pack(padx=10, pady=10)
    forest.pack(padx=10, pady=10)
    home.pack(padx=10, pady=10)

def AddShops():
    blacksmith.pack(padx=10, pady=10)
    farmer.pack(padx=10, pady=10)
    wizard.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)

def AddMiniS():
    leather.pack(padx=10, pady=10)
    apple.pack(padx=10, pady=10)
    meat.pack(padx=10, pady=10)
    sword.pack(padx=10, pady=10)
    sheild.pack(padx=10, pady=10)
    chainmail.pack(padx=10, pady=10)
    axe.pack(padx=10, pady=10)
    sword.pack(padx=10, pady=10)
    ale.pack(padx=10, pady=10)
    Tmeat.pack(padx=10, pady=10)
    Tsleep.pack(padx=10, pady=10)
    sleep.pack(padx=10, pady=10)
    craft.pack(padx=10, pady=10)
    WatPouch.pack(padx=10, pady=10)
    OHP.pack(padx=10, pady=10)
    THP.pack(padx=10, pady=10)
    FHP.pack(padx=10, pady=10)
    water.pack(padx=10, pady=10)
    consume.pack(padx=10, pady=10)
    appleC.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)


def ChangeState(newState):
    global State;
    State = newState;
    if State == 1:
        AddPlaces()
        TMeat = 0
        Ale = 0
    elif State == 2:
        AddShops()
        TMeat = 0
        Ale = 0

def RunGame():
    global HP
    global Max_HP
    if HP > Max_HP:
        HP = Max_HP
    elif State == 0:
        AddHouses()
    elif LossHP == random.randint(1,10):
        HP = HP - 1
        print("You have ",HP,"HP left.")
    elif State > 0:
        temp="Sleep, restore", SleepHeal,"HP"
    elif Money < 0:
        print("You're bankrupt!")
    elif HP < 1:
        print("You died!")
        
    
def DestroyAllS():
    blacksmith.pack_forget()
    farmer.pack_forget()
    wizard.pack_forget()
    craft.pack_forget()
    sleep.pack_forget()
    leave.pack_forget()
def DestroyAllP():
    shop.pack_forget()
    tavern.pack_forget()
    well.pack_forget()
    forest.pack_forget()
    home.pack_forget()
def DestroyAllH():
    House1.pack_forget()
    House2.pack_forget()
    House3.pack_forget()
    House4.pack_forget()
def DestroyAllM():
    leather.pack_forget()
    apple.pack_forget()
    bread.pack_forget()
    meat.pack_forget()
    sword.pack_forget()
    sheild.pack_forget()
    chainmail.pack_forget()
    sword.pack_forget()
    axe.pack_forget()
    ale.pack_forget()
    Tmeat.pack_forget()
    Tsleep.pack_forget()
    sleep.pack_forget()
    WatPouch.pack_forget()
    OHP.pack_forget()
    THP.pack_forget()
    FHP.pack_forget()
    fight.pack_forget()
    tree.pack_forget()
    water.pack_forget()
    consume.pack_forget()
    appleC.pack_forget()
    Ale = 0
    TMeat = 0
    leave.pack_forget()

def onClickShop(event):
    DestroyAllP()
    print("Where to shop?")
    ChangeState(2)
    RunGame()
def onClickTavern(event):
    DestroyAllP()
    global leave
    Tmeat.pack(padx=10, pady=10)
    ale.pack(padx=10, pady=10)
    Tsleep.pack(padx=10, pady=10)
    consume.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)
    RunGame()
def onClickWell(event):
    DestroyAllP()
    global leave
    if watrP > 0:
        water.pack(padx=10, pady=10)
    else:
        print("You can't do anything here yet.")
    leave.pack(padx=10, pady=10)
    RunGame()
def onClickForest(event):
    DestroyAllP()
    global leave
    fight.pack(padx=10, pady=10)
    tree.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)
    RunGame()
def onClickHome(event):
    print("You're home.")
    DestroyAllP()
    global craft
    global sleep
    global leave
    craft.pack(padx=10, pady=10)
    sleep.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)
    consume.pack(padx=10, pady=10)
    global TMeat
    global Ale
    TMeat = 0
    Ale = 0
    RunGame()
def onClickBlacksmith(event):
    DestroyAllS()
    global leave
    sword.pack(padx=10, pady=10)
    sheild.pack(padx=10, pady=10)
    chainmail.pack(padx=10, pady=10)
    axe.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)
    RunGame()
def onClickFarmer(event):
    DestroyAllS()
    global leave
    leather.pack(padx=10, pady=10)
    apple.pack(padx=10, pady=10)
    bread.pack(padx=10, pady=10)
    meat.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)
    RunGame()
def onClickWizard(event):
    DestroyAllS()
    global leave
    OHP.pack(padx=10, pady=10)
    THP.pack(padx=10, pady=10)
    FHP.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)
    RunGame()
def onClickCraft(event):
    DestroyAllS()
    global leave
    WatPouch.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)
    RunGame()
def onClickSleep(event):
    global HP
    if HP < Max_HP:
        print("Your nap was so good, you restored ",SleepHeal,"HP!")
        HP = HP + SleepHeal
    else:
        print("You're not tired.")
    RunGame()
def onClickTsleep(event):
    global HP
    global Money
    if HP < Max_HP:
        print("Your nap was so good, you restored 12HP!")
        HP = HP + SleepHeal
        Money = Money - 7
    else:
        print("You're not tired.")
    RunGame()
def onClickLeather(event):
    global Leather
    global Money
    Leather = Leather + 1
    Money = Money - 2
    print("You have ",Leather,"sheets of leather!")
    RunGame()
def onClickApple(event):
    global Apple
    global Money
    Apple = Apple + 1
    Money = Money - 3
    print("You have ",Apple,"apples!")
    RunGame()
def onClickBread(event):
    global Bread
    global Money
    Bread = Bread + 5
    Money = Money - 15
    print("You have ",Bread / 5,"loaves of bread!")
    RunGame()
def onClickMeat(event):
    global Meat
    global Money
    Meat = Meat + 1
    Money = Money - 10
    print("You have ",Meat,"sides of meat!")
    RunGame()
def onClickSword(event):
    global Sword
    global Attack
    global Money
    if Sword > 0:
        print("You already have a sword")
    else:
        Sword = 1
        Attack = Attack + 20
        Money = Money - 30
        print("You got a sword!")
    RunGame()
def onClickSheild(event):
    global Sheild
    global Armour
    global Money
    if Sheild > 0:
        print("You already have a sheild")
    else:
        Sheild = 1
        Armour = Armour + 12
        Money = Money - 15
        print("You got a sheild!")
    RunGame()
def onClickChainM(event):
    global ChainM
    global Armour
    global Money
    if ChainM > 0:
        print("You already have chainmail")
    else:
        Armour = Armour + 28
        Money = Money - 40
        print("You got some chainmail!")
    RunGame()
def onClickAxe(event):
    global Axe
    global Money
    if ChainM > 0:
        print("You already have an axe")
    else:
        Axe = 1
        Money = Money - 20
        print("You got an axe!")
    RunGame()
def onClickOHP(event):
    global Max_HP
    global HP
    global Money
    Max_HP = Max_HP + 1
    HP = Max_HP
    Money = Money - 100
    print("Your max life was increased to ", Max_HP,"!")
    RunGame()
def onClickTHP(event):
    global Max_HP
    global HP
    global Money
    Max_HP = Max_HP + 3
    HP = Max_HP
    Money = Money - 300
    print("Your max life was increased to ", Max_HP,"!")
    RunGame()
def onClickFHP(event):
    global Max_HP
    global HP
    global Money
    Max_HP = Max_HP + 5
    HP = Max_HP
    Money = Money - 500
    print("Your max life was increased to ", Max_HP,"!")
    RunGame()
def onClickTmeat(event):
    global TMeat
    global Money
    TMeat = TMeat + 1
    Money = Money - 8
    print("You have ",TMeat,"sides of tavern meat")
    RunGame()
def onClickAle(event):
    global Ale
    global Money
    Ale = Ale + 1
    Money = Money - 6
    print("You have ",Ale,"pints of ale")
    RunGame()
def onClickWatPouch(event):
    global Water
    global watrP
    global Leather
    if Leather > 2 and watrP == 0:
        watrP = watrP + 1
        Water = 10
        Leather = Leather - 3
        print("You got a water pouch!")
    elif watrP >0:
        print("You already have a water pouch.")
    else:
        print("You don't have enough leather to craft this item.")
    RunGame()
def onClickWater(event):
    global Water
    if Water < 10:
        Water = 10
        print("You refilled your water pouch")
    else:
        print("Your water pouch is already full.")
    RunGame()
def onClickConsume(event):
    if Apple > 0:
        appleC.pack(padx=10, pady=10)
    if Bread > 0:
        breadC.pack(padx=10, pady=10)
    if Meat > 0:
        meatC.pack(padx=10, pady=10)
    if TMeat > 0:
        TmeatC.pack(padx=10, pady=10)
    if Ale > 0:
        aleC.pack(padx=10, pady=10)
    if Water > 0:
        waterC.pack(padx=10, pady=10)
    leave.pack(padx=10, pady=10)
    RunGame()
def Consume(HPgain):
    global HP
    HP += HPgain
    if (HP > 100):
        HP = 100
    print ("You're full.")
def onClickAppleC(event):
    global Apple
    if Apple < 1:
        print("You don't have any apples left")
    else:
        HPgain = 5
        Apple -= 1
        print("You ate an apple!")
    RunGame()
def onClickBreadC(event):
    global Bread
    if Bread < 1:
        print("You don't have any bread left")
    else:
        HPgain = 3
        Bread -= 1
        print("You ate a slice of bread!")
    RunGame()
def onClickMeatC(event):
    global Meat
    if Meat < 1:
        print("You don't have any meat left")
    else:
        HPgain = 10
        Meat -= 1
        print("You ate a side of meat!")
    RunGame()
def onClickAleC(event):
    global Ale
    if Ale < 1:
        print("You don't have any ale left")
    else:
        HPgain = 5
        Ale -= 1
        print("You drank some ale!")
    RunGame()
def onClickTmeatC(event):
    global TMeat
    if TMeat < 1:
        print("You don't have any meat left")
    else:
        HPgain = 10
        TMeat -= 1
        print("You ate a side of meat!")
    RunGame()
def onClickWaterC(event):
    global Water
    if Water < 1:
        print("You don't have any water left")
    else:
        HPgain = 4
        Water -= 1
        print("You drank some water!")
    RunGame()
blacksmith = tkinter.Button(Game, text="Blacksmith's shop", width = 40)
farmer = tkinter.Button(Game, text="Farmer's shop", width = 40)
wizard = tkinter.Button(Game, text="Wizard's shop", width = 40)
craft = tkinter.Button(Game, text="Craft", width = 40)
sleep = tkinter.Button(Game, text="Sleep", width = 40)
leave = tkinter.Button(Game, text="Leave", width = 40)
leather = tkinter.Button(Game, text="Leather, 2 gold, material", width = 40)
apple = tkinter.Button(Game, text="Apple, 3 gold, restores 5HP", width = 40)
bread = tkinter.Button(Game, text="1 loaf (5 slices)of bread, 15 gold, restores 3HP per slice", width = 40)
meat = tkinter.Button(Game, text="Meat, 10 gold, restores 10HP", width = 40)
sword = tkinter.Button(Game, text="Sword, 30 gold, 20 damage", width = 40)
sheild = tkinter.Button(Game, text="Sheild, 15 gold, 12 armour", width = 40)
chainmail = tkinter.Button(Game, text="Chainmail, 40 gold, 28 armour", width = 40)
axe = tkinter.Button(Game, text="Axe, 20 gold", width = 40)
OHP = tkinter.Button(Game, text="+1 new HP, 100 gold", width = 40)
THP = tkinter.Button(Game, text="+3 new HP, 300 gold", width = 40)
FHP = tkinter.Button(Game, text="+5 new HP, 500 gold", width = 40)
Tmeat = tkinter.Button(Game, text="Meat, 8 gold, restores 10HP", width = 40)
ale = tkinter.Button(Game, text="Ale, 6 gold, restores 5HP", width = 40)
Tsleep = tkinter.Button(Game, text="Sleep, 7 gold, restores 12HP", width = 40)
sleep = tkinter.Button(Game, text=temp, width = 40)
WatPouch = tkinter.Button(Game, text="Craft water pouch, 3 leather", width = 40)
water = tkinter.Button(Game, text="Refill water pouch", width = 40)
fight = tkinter.Button(Game, text="Fight an enemy", width = 40)
tree = tkinter.Button(Game, text="Cut down trees", width = 40)
shop = tkinter.Button(Game, text="Shop", width =40)
tavern = tkinter.Button(Game, text="Tavern", width =40)
well = tkinter.Button(Game, text="Well", width =40)
forest = tkinter.Button(Game, text="Forest", width =40)
home = tkinter.Button(Game, text="Home", width =40)
consume = tkinter.Button(Game, text="Eat or drink", width =40)
appleC = tkinter.Button(Game, text="Eat an apple", width =40)
breadC = tkinter.Button(Game, text="Eat a slice of bread", width =40)
meatC = tkinter.Button(Game, text="Eat a side of meat", width =40)
TmeatC = tkinter.Button(Game, text="Eat a side of meat", width =40)
aleC = tkinter.Button(Game, text="Drink some ale", width =40)
waterC = tkinter.Button(Game, text="Drink some water", width =40)
if State == 1:
    print("Where do you want to go?")
    AddPlaces()

shop.bind("<ButtonRelease-1>", onClickShop)
tavern.bind("<ButtonRelease-1>", onClickTavern)
well.bind("<ButtonRelease-1>", onClickWell)
forest.bind("<ButtonRelease-1>", onClickForest)
home.bind("<ButtonRelease-1>", onClickHome)
blacksmith.bind("<ButtonRelease-1>", onClickBlacksmith)
farmer.bind("<ButtonRelease-1>", onClickFarmer)
wizard.bind("<ButtonRelease-1>", onClickWizard)
craft.bind("<ButtonRelease-1>", onClickCraft)
sleep.bind("<ButtonRelease-1>", onClickSleep)
leave.bind("<ButtonRelease-1>", Leave)
Tsleep.bind("<ButtonRelease-1>", onClickTsleep)
leather.bind("<ButtonRelease-1>", onClickLeather)
apple.bind("<ButtonRelease-1>", onClickApple)
bread.bind("<ButtonRelease-1>", onClickBread)
meat.bind("<ButtonRelease-1>", onClickMeat)
sword.bind("<ButtonRelease-1>", onClickSword)
sheild.bind("<ButtonRelease-1>", onClickSheild)
chainmail.bind("<ButtonRelease-1>", onClickChainM)
axe.bind("<ButtonRelease-1>", onClickAxe)
OHP.bind("<ButtonRelease-1>", onClickOHP)
THP.bind("<ButtonRelease-1>", onClickTHP)
FHP.bind("<ButtonRelease-1>", onClickFHP)
Tmeat.bind("<ButtonRelease-1>", onClickTmeat)
ale.bind("<ButtonRelease-1>", onClickAle)
sleep.bind("<ButtonRelease-1>", onClickSleep)
WatPouch.bind("<ButtonRelease-1>", onClickWatPouch)
water.bind("<ButtonRelease-1>", onClickWater)
appleC.bind("<ButtonRelease-1>", onClickAppleC)
breadC.bind("<ButtonRelease-1>", onClickBreadC)
meatC.bind("<ButtonRelease-1>", onClickMeatC)
TmeatC.bind("<ButtonRelease-1>", onClickTmeatC)
aleC.bind("<ButtonRelease-1>", onClickAleC)
waterC.bind("<ButtonRelease-1>", onClickWaterC)
consume.bind("<ButtonRelease-1>", onClickConsume)
RunGame()
