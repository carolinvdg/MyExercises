import time
global money
global monkeys
gold = 0
gold = 0

def start ():
    print "Welcome to the jungle"
    name = raw_input ("What is your jungle name?")
    print "Good luck, "+name+"!"
    print "In this game you have to find monkeys and sell them"
    choice = raw_input ("Wanna play? YES or NO?")
    if play == "YES":
         begin ()
    if play == "NO":
       print "Bye then"

def begin () :
    global monkeys
    global money
    print "Lets go"
    if money > 99:
       print "You won the game"
       play = raw_input ("Do you want to play again? YES or NO")
       if play == "YES"
             begin ()
       if play =="NO"
          print "Bye then"

     pick = raw_input ("Do you want to pick up a monkey? YES/NO")
      if pick == "YES"
           time.sleep (1)
           print "You picked up a monkey"
           monkey=monkeys+1
           print "You have ",monkeys," monkeys"
           begin ()
      if pick == "NO"
         sell = raw_input ("Do you wanna sell the monkeys? YES or NO")
         if sell == "YES" :
         global money
         global monkey
         print "You currently have, ",monkeys," monkeys"
         print "You have sold your monkeys"
         money=monkey*10
         monkeys=0
         print "You have now:",money,
         begin ()
