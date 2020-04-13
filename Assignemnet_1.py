# A class for people to come up with their own Horoscopes for
# A self made-up Astrologic signs
# Give the class a couple things to make a Horoscope
# Maybe stuff like a symbol, if they are going to find love,
# Lucky colour, how they will die, how other see them
# Whether or not they will be happy or succeed 
#
# Program Needs: 
# ?Prompts or some code for the name, the "predictions", the dates for the
# Self made-up sign.
# A formatter for giving the Horoscope
# A quit out checker as per instruction 


import random


class Astrology_Class():
    
    def __init__(Self, When, Future, Death, Personality):
        Self.Symbol = input(f"Please describe a symbol to be associated with {Self}:")
        Self.Date = When[random.randint(0,12)]
        Self.Prediction = Future[random.randint(0,9)]
        Self.Death = Death[random.randint(0,11)]
        Self.Personality = Personality[random.randint(0,16)] + " and " + Personality[random.randint(8,16)] 

    def Whole_Horoscope(Self):
        Horoscope = f"Horoscope for {Self}: \n"
        Horoscope += f"The symbol for {Self} is {Self.Symbol}."
        Horoscope += f"The stars have this to say for you: \n\t\"{Self.Prediction}\"\n"
        Horoscope += f"The stars say your death will be by: \n\t\"{Self.Death}\"\n"
        Horoscope += f"People who are {Self} tend to be {Self.Personality}."

def Main():
    Dates = [
        "March 21th - April 19th",
        "April 20th - May 20th",
        "May 21st - June 20th",
        "June 21st - July 22nd",
        "July 23rd - Aug 22nd",
        "Aug 23rd - Sept 22nd",
        "Sept 23rd - Oct 22nd",
        "Oct 23rd - Nov 21st",
        "Nov 22nd - Dec 21st",
        "Dec 22nd - Jan 19th",
        "Jan 20th - Feb 18th",
        "Feb 19th - March 20th"
    ]

    Predictions = [
        "Today, it's not about figuring out what other people can do to make you happy.",
        "There is a lot of love swirling around you today, so why don't you reach out and get some of it.",
        "Talking and socializing could take up a lot of your day.",
        "A very small detail could derail some of your plans today.",
        "Pay close attention to any feedback you're given today.",
        "Planning can be a lot of fun for you today, especially if the details involved are small ones.",
        "Some good news could send your mood skyrocketing!",
        "Make sure you do your research today. Know the ins and outs.",
        "Be extremely careful about the people you get involved with right now"
    ]

    Traits = [
        "Articulate",
        "Calm",
        "Caring",
        "Charming",
        "Focused",
        "Generous",
        "Herioc",
        "Honest",
        "Kind",
        "Loyal",
        "Organized",
        "Patient",
        "Self-Critical",
        "Strong-willed",
        "Trusting",
        "Witty",
    ]

    Deaths = [
        "Smothered to death by gifts of cloaks and hats showered upon him by appreciative friends",
        "Murdered by political enemies.",
        "Devoured by dogs after smearing themself with cow manure.",
        "Over consumption of bull's blood.",
        "Head trama caused by a tortised dropped by an eagle hitting their head.",
        "Leaping into an active volcano to prove they are an imortal god.",
        "Choke on an unripe grape while trying to snack while delivering a monologue before The King",
        "Using a poisoned toothpick",
        "Laughing too much",
        "Intentionally swallowing hot coals",
        "The 5th assassin sent by The Queen",
    ]

    MainMenu = "Please enter the number for the menu option you want to do\
        1\tCreate an Astrologic Sign \n2\tLook at previously created Astrologic Signs \n3\tQuit"