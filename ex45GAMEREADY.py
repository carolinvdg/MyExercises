from sys import exit
from random import randint


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Scene (object):

    def enter(self):
        print "?"
        exit (1)



class Munich (Scene):
    def enter(self):
        print "Your journey starts in the very south of Germany. In the most stuffy city there is. "
        print "You are in Munich, where every store closes at 8 o clock. "
        print "You need to get out"
        print "\n"
        print "In order to flee the city, you need a cheap ride out."
        print "So what do you wanna do?"
        print "You can either HITCHHIKE or take the TRAIN without buying a ticket and hope for the best"


        choice = raw_input("> ")
        if choice == "HITCHHIKE":
            return 'Frankfurt'

        elif choice == "TRAIN":
            return 'HANNOVER'

        else:
            print "Stick to your options!"
            return 'MUNICH'


class Frankfurt(Scene):
    def enter (self):
        print "Welcome to Frankfurt. You need a place to spend the night."
        print "You can choose between finding accomodation on TINDER or sleep at TRAINSTATION"

        choice = raw_input("> ")
        if choice == "TINDER":
            print "Wow, you are so lucky."
            print "Found someone who is handsome AND a great cook"
            print "You sepend a lovely night at your Tinder date's place"
            print "You sleep very well. The next morning breakfast is prepared for you."
            print "You tell your date, that you need to get out of the city."
            print "Luckily your tinder date's mom is driving to HANNOVER today."
            print "You can join."
            return 'HANNOVER'

        elif choice == "TRAINSTATION":
            print "Are you mad?"
            print "This is Frankfurt! Hookers steal your phone and you get beaten up by addicts."
            print "You are not going anywhere. You die."
            return 'death'

        else:
            print "Stick to your choices!"
            return 'Frankfurt'

class Hannover(Scene):
    def enter (self):
        print "You made it to the busiest Train Station"
        print "Thats good. You can go nearly anywhwere from here"
        print "But you are still out of money. "
        print "You need to earn some cash."
        print "You can either BEG for money or ROB a bank"

        choice = raw_input("> ")
        if choice == "BEG":
            print "The real hobos get really mad and punch you hard"
            print "You die"
            return 'death'

        elif choice == "ROB":
            print "Are you mad?"
            print "You really wanna go through with this, you are insane"
            print "You cover your face with a scarf and go to the bank"
            print "The lady at the counter thinks you are joking."
            print "You know her from vacation"
            print "She sais: Nice to see you again! Haha, good joke!"
            print "You ask her to lend you money, she agrees. How much money do you need?"


            choice = raw_input("> ")
            how_many = int (choice)

            if how_many <20:
                print "You are not getting anywhere with that."
                print "You have to sleep at the station and die from a lung infection after a night on the cold stone"
                return 'death'
            else:
                print "Get on the train again."
                print "Do you want to get out at LUNEBURG or BREMEN ?"

                choice = raw_input("> ")
                if choice == "LUNEBURG":
                    print "You chose the most boring city in Germany to stop at"
                    return 'LUNEBURG'

                elif choice == "BREMEN":
                    print "Okay, hope you brought a nice and warm jacket, its very cold at the harbor "
                    return 'BREMEN'

                else:
                    print "Stick to your options."
                    return 'HANNOVER'

        else:
            print "Stick to sour options."
            return 'HANNOVER'


class LUNEBURG(Scene):
    def enter (self):
        print "You came during Lunatic. Lucky you. Its the best time to be around Luneburg"
        print "There are some pretty amazing acts."
        print "You manage to trick the bouncer and get in without paying,"
        print "Pretty amazing work! What could possibly go wrong from now on?"
        print "You can choose an act! Do you wanna see VONWEGENLISBETH or MONEYBOY?"

        choice = raw_input ("> ")
        if choice == "MONEYBOY":
            print "You chose the king of our generation. You will love the show"
            print "Oh no! Moneyboy seems to be out of his mind!"
            print "He took a few drugs too many!"
            print "Be careful, he is throwing the microphone into the crowd!"
            print "It hits you right on the head. You die immediately."
            return 'death'

        elif choice == "VONWEGENLISBETH":
            print " What an amazing show! You love them!"
            print "You even get the chance to talk to them after the show."
            print "Wow, seems like they really like you. They have another gig in BREMEN and allow you to join the tour bus"
            return 'BREMEN'

        else:
            print "Stick to your options."
            return 'LUNEBURG'


class BREMEN (Scene):
    def enter (self):
        print 'Here you are! Its cold and you are hungry.'
        print "What to get:"

        dishes = "FISHBUN, WAFFLES, BOOZE"
        print dishes
        print "Do you want something savory,something sweet or rather get drunk?"
        print "What do you wanna get?"

        choice = raw_input("> ")
        if choice == "FISHBUN":
            print "Good choice."
            print "In Bremen you can get good fish!"
            print "But what kind of fish would you like?"
            print "Do you want MATIE or FRIEDFISH?"

            choice = raw_input("> ").upper
            if choice == "FRIEDFISH":
                print "Oh no. The fish wasnt good anymore. The flaky crust covered up the bad taste"
                print "You die of food poisoning."
                return 'death'
            elif choice == "MATIE":
                print "That tastes great! You compliment the little fish shop"
                print "The worker at the fish job is very happy about the compliment"
                print "He tells you that he wants to open a shop in the best city in the world."
                print "Then he grins like he is thinking about something"
                print "I have a great idea, he sais. Would you like to work in the fish store in COLOGNE ?"
                print "You cannot believe it. You would love to!"
                return 'COLOGNE'


        elif choice =="WAFFLES":
            print "Sometimes an unhealthy treat is all you need."
            print "The waffles are insanely big and look delicious."
            print "You can get CHOCOLATE or SURPRISE waffles "

            choice = raw_input("> ")
            if choice == "CHOCOLATE":
                print "Oh no! You accidentally spill the sauce all over your clothes"
                print "You look pathetic. No one likes you. You die of stupidity"
                return 'death'
            elif choice == "SURPRISE":
                print "Good choice!"
                print "A siren in the waffle store starts blinking"
                print "Whats the matter?"
                print "You ordered the 1000th surprise waffle and therefore get a big surprise"
                print "You win a trip to th best city in the world!"
                return 'COLOGNE'
            else:
                print "Stick to your choices"
                return 'BREMEN'


        elif choice == "BOOZE":
            print "You just know how to turn a bad day into a good one."
            print "Being tipsy helps dealing with the cold weather"
            print "And you appear to be an absolute great entertainer when drinking"
            print "You tell jokes loudly and a big crowd surrounds you."
            print "They cheer, you are amazing!"
            print "Then they even start collecting money for you. Great! "
            print "One of the men in the crowd turns out to be an agent. He offers you a contract and a ride to the best city in the world."
            print "You can fly out to COLOGNE"
            return 'COLOGNE'
        else:
            print "Stick to your choices!"
            return 'BREMEN'


class Bus(Scene):
    def enter (self):
        print "Congrats, you made it to Cologne!"
        print "I hope you learned something out of this!"
        print "Dont go on a huge trip without any money!"
        print "But you arrived- thats all that matters!"
        print "Right in time for carnival. Do you want to dress up as the STATUEOFLIBERTY or HANNAHMONTANA ?"

        choice = raw_input ("> ")
        if choice == "HANNAHMONTANA":
            print "You look just like her!"
            print "Amazing! You have great fun!"
            return 'END'



        elif choice == "STATUEOFLIBERTY":
            print "Everyone thinks you are a Trump supporter and is very mean"#
            print "You get kicked out of every party"
            print "No one likes you. You managed to have the worst time in the best city."
            return 'death'


class Death(Scene):
    quips = [
    "You're not made for these kinds of journey. Go home and cry"
    ]



class END(Scene):
    def enter (self):
        print "You had an amazing adventure."
        print "What a trip!"
        print "You won in life."



class Map (object):

    scenes ={
    'MUNICH': MUNICH(),
    'FRANKFURT': FRANKFURT(),
    'HANNOVER': HANNOVER(),
    'LUNEBURG': LUNEBURG(),
    'BREMEN': BREMEN(),
    'COLOGNE': COLOGNE(),
    'death': Death(),
    'END': END(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene (self):
        return self.next_scene(self.start_scene)

a_map = Map ('MUNICH')
a_game = Engine(a_map)
a_game.play()
