class Scene(object):
camping_site = Scene("Carnival Cologne", "carnival_cologne",

"""Its your first time to celebrate carnival in Cologne! You have heard a lot about it!
Today you are going to meet friends and have an amazing time! But first you have to chose a costume!
You can either go for a chicken costume or Lara Croft! What do you wanna pick?
"""
)

carnival_cologne_chicken = Scene("Carnival Cologne Costume", "carnival_cologne_laracroft",
"""
The chicken costume it is! Nice one! Its funny looking. You dont want to go as a sexy Lara Croft
and prefer the fun version! Good on you. Who knows how the drunk guys would have reacted for the Lara Croft costume.
You can either wear a hoodie or none under the chicken costume. Do you want to check the weather online or just go without checking?
"""
)

laracroft_choice = Scene ("Lara Croft", "laracroft_choice",
""")
Oh, you want to look sexy.
Thats a risky thing to do!
These days everyone is incredibly drunk.
But therefore you look better than if you chose the chicken costume.
You put the costume on and are pumped for the night.
Where do you want to go? To Zülpicher Platz or to Chlodwigplatz?
""")

carnival_cologne_death = Scene ("Death...", "carnival_cologne_death",
"""
Oh no. You decided to go without a sweater on, because you didnt check
the weather. That is the dumbest thing I have ever heard.
ALLWAYS bad weather on carnival, you know?
You die of freezing to death.
""")

Zülpicherplatz = Scene ("Zülpicher Platz", "zülpicher_platz",
"""
Okay, you picked Zülpicher Platz! Thats where all the students go.
You are right in the center of university life. Surprisingly the behave well and
you do not get in an unpleasent situation. The opposite is the case!
The first bar you go into, a nice guy offers to buy you shots if you can guess
what kind of queen he has in his pocket.
Clubs, Spades, Diamonds or Heart?
""")

Chlodwigplatz = Scene ("Chlodwigplatz", "chlodwig_platz",
"""

Okay, perfect! Allways something going on at Clodwigplatz!
Do you want to go to a bar or just stay in the streets for the good old traditional
carnival?

""")

chlodwig_platz_death= Scene ("Death...", "chlodwig_platz_death",
"""
Oh no! The bar is owned by a Bavarian. They do not listen to carnival music, 
but to ApresSki-hits instead. You die of ear cancer.
"""
)



diamond_card = Scene("Diamond Card", "diamond_card",
"""
You look the guy deep in the eye and decide to go for the diamond card:
The guy starts smiling at you and reveals his card. Its a queen of diamonds.
Nice job!
You get granted a shot and a beer. A nice conversation is included"
""")

diamond_card_win = Scene("Tennis Ball Win", "tennis_ball_win",
"""
Cool! The conversation is very smooth. You kind of like the guy.
He offers for you and your friends to keep partying at his house!
Do you want to come with him or check a bar out instead?

"""
)

heart_card_death = Scene("Death...", "heart_card_death",
"""
You think it is a card with hearts.
Sounds the most logic! Its the flirtiest sign, right?
The guy is annoyed by that obvious choice.
He leaves you.
Ypou die of heartbreak.
""")

spades_card = Scene("Spades Card", "spades_card",
"""
You think it is a card with spades.
The guy looks at you and starts smiling.
Its the wrong card.
But he doesnt care and tells you to order a drink anyway.
Amazing! You picked the wrong card but still get a drink for free!
""")

clubs_card_death = Scene ("Death...", "clubs_card_death",
"""
You go for Clubs!
The guy reveals his card.... and.... you made the wrong choice!
Unfortunateöly he will not get you a drink.
Unfortunate! You were really looking forward to having a drink with him.
You die of a broken heart,
""")

guys_house = Scene ("Guys House", "guys_house",
"""
Okay, you decided to go to the guys house!
He studies geography.
And when you and your friends agree to come, he suddenly hesitates.
He wants to know if you are interested in the same stuff he is.
So he lets you take capital city quiz.
He picks for differnet countries and you have to know at least one capital city:

1: Albania
2: Croatia
3: NewZealand
4: Southkorea
Do you choose riddle 1,2,3 or 4?

""")

riddle_one = Scene ("Riddle One", "riddle_one",
"""
Whats the capital city of Albania?
...
What's your answer?
"""
)

riddle_two = Scene ("Riddle Two", "riddle_two",
"""
Whats the capital city of Croatia?
...
What's your answer?
"""
)

riddle_three = Scene ("Riddle Three", "riddle_three",
"""
Whats the capital city of NewZealand?
...
What's your answer?
"""
)

riddle_four = Scene ("Riddle Four", "riddle_four",
"""
Whats the capital city of Southkoea?
...
What's your answer?
"""
)

guys_house_death = Scene ("Death...", "guys_house_death",
"""
Really?
You are an absolute idiot! You are an embarassment. The guy
does not want you in his house."""
)

journey_to_house = Scene ("Journey to house", "journey_to_house",
"""
Okay you are excited for the place the guy lives in.
It is in Rodenkirchen, which is a very nice part of th ecity. But therefore its
a far way. How do you want to go there?
Take a taxi or go by train?

"""
)

taxi_choice = Scene ("Taxi choice", "taxi_choice",
"""
You take a taxi. Unfortunately the drivers taxometer is broken. But there
is no other taxi around! he wants you to tip him.
The tip must consist of three numbers between 1 and 3.
There is no number twice.
"""
)



drinks_selection = Scene ("Drinks drinks_selection", "drinks_selection",
"""
The place is amazing!
The guy invites some othe friends over.
His parents are there too! But they seem to be party animals as well.
The whole place turns into a huge party!
The mother offers homemade cherry schnaps. Or you can just stick to beer.
What do you do?
"""
)

cherry_schnaps = Scene ("Cherry Schnaps", "cherry_schnaps",
"""
Wow! Brave choice.
The mother is very excited for you to drink the schnaps. You assume that it
will be very hard on you. She pours 2. Do you want to drink both?
What do you chose, 1 or 2?

"""
)

overall_good_time = Scene ("Overall good time", "Overall_good_time",
"""
Nice! You pour liek a boss!
Yoiu party like a real Cologne Badass! Carnival was teh best thing you have done in a while!
Surely you will be back next year.
"""
)

death_carnival= Scene ("Death carnival", "death_carnival",
"""
Maan, who do you think you are?
You come to Cologne like you one cool guy and then you just embarass yourself!
What a shame!
We dont need guys like you to party here.
LEAVE
"""
)


})

carnival_cologne.add_paths({
    'laracroft':laracroft_choice,
    'chicken':carnival_cologne_death

})

laracroft_choice.add_paths({
    'zülpicherplatz': zülpicher_platz,
    'chlodwigplatz': chlodwig_platz

})

zülpicher_platz.add_paths({
    'diamond': diamond_card,
    'heart':heart_card_death,
    'spades':spades_card,
    'Clubs':clubs_card_death,


})

chlodwig_platz.add_paths({
    'bar': zülpicher_platz
    'traditional carnival': chlodwig_platz_death


})

guys_house.add_paths({
    '1': riddle_one,
    '2': riddle_two,
    '3': riddle_three,
    '4': riddle_four
})

riddle_one.add_paths({
    'Tirana': way_to_festival,
    '*': neon_colors_death
})

riddle_two.add_paths({
    'zagreb': way_to_festival,
    '*': guys_house_death
})

riddle_three.add_paths({
    'canberra': way_to_festival,
    '*': guys_house_death
})

riddle_four.add_paths({
    'seoul': way_to_festival,
    '*': guys_house_death
})

journey_to_house.add_paths({
    'taxi': taxi_choice,
    'train': taxi_choice_death
})



drinks_selection.add_paths({
    '1': total_win,
    '2': death_carnival
})
SCENES = {
     carnival_cologne_chicken :chicken
    carnival_cologne_chicken.urlname : camping_site_chicken,
    carnival_cologne_death.urlname : carnival_cologne_death
    chlodwig_platz.urlname: chlodwig_platz_death
    diamond_card: diamond_card,
    heart-Card.urlname: heart_card_death,
    spades_card.urlname: spades_card,
    cross_card.urlname: cross_card_death
    guys_house.urlname: guys_house,
    riddle_one.urlname: riddle_one,
    riddle_two.urlname: riddle_two,
    riddle_three.urlname: riddle_three,
    riddle_four.urlname: riddle_four,
    guys_house.urlname: guys_house_death,
    journey_to_house.urlname: journey_to_house,
    cherry_schnaps.urlname: cherry_schnaps,
    overall_good_time.urlname: overall_good_time,
    drinks_selection.urlname: drinks_selection,
    death_carnival.urlname: death_carnival


}
START = carnival_cologne
