import speech_recognition as sr
import pyttsx3
import random

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")

engine.setProperty("voices", voice[2].id)
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)


def Voice(auido):
    engine.say(auido)
    engine.runAndWait()


def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.energy_threshold = 500

        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-In")
        # print(f"Boss siad: {query}\n")
    except Exception as e:
        sen = "Command not match"
        # print(sen)

        return ""
    return query


def rockPaperScissor(voice=Voice):
    voice("Ok Boss, Firstly understand the rules")
    rules = " Boss your match will be with computer means Of course with me . This match is of 10 rounds and each round contains 10 points. The player who scores more points than the opponent player then that player will win. Note one thing: if any round ends in a tie, that round will be considered. Best of luck Boss."
    voice(rules)
    # Voice("it will take few seconds please wait..")
    # time.sleep(2)

    voice(
        " Boss their are three options first one is Rock second one is paper and  third one is Scissor. You have to choose only one of them. When I Voice 'Rock Paper Scissors,' you must then tell me your choice."
    )
    # time.sleep(3)
    round = 0
    score = 0
    userScore = 0
    compScore = 0
    tie = 0
    while not (round == 10):
        # This is computers choise
        opt = ["rock", "paper", "scissor", "paper", "scissor", "rock"]
        Comp = random.choice(opt)
        # print("Compute choise :" + Comp)
        num = [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
            "last",
        ]
        if round < 9:
            voice("This is Round number " + num[round])
        else:
            voice(" Boss this is your " + num[round] + "Round")

        voice("Rock paper Scissor")
        user = takeComand().lower()
        if not (
            "rock" in user
            or "frock" in user
            or "paper" in user
            or "scissor" in user
            or "caesar" in user
        ):
            voice("Boss you should choose  Rock or Paper or Scissor")
            round -= 1

        User = None
        if "rock" in user or "frock" in user:
            User = "rock"
        elif "paper" in user:
            User = "paper"
        elif "scissor" in user or "caesar" in user:
            User = "scissor"

        # print(User)
        round += 1

        if User == Comp:
            voice(
                f"Boss this Round is tie you choose {User} and i choose {Comp} : So now the precidence of our power is same"
            )
            score += 10
            tie += 1
        elif (
            User == "rock"
            and Comp == "scissor"
            or User == "paper"
            and Comp == "rock"
            or User == "scissor"
            and Comp == "paper"
        ):
            voice(
                f"  Wow : congratulations you have won this round. you choose {User} and i  choose{Comp}"
            )
            userScore += 10

        elif (
            Comp == "rock"
            and User == "scissor"
            or Comp == "paper"
            and User == "rock"
            or Comp == "scissor"
            and User == "paper"
        ):
            voice(
                f"Oops unfortunately you lose this round: You choose {User} and i Choose {Comp}"
            )
            compScore += 10

    voice(
        "As I told you this match will be of 10 rounds and those 10 rounds are now complete : Now let's see whose score is higher"
    )
    voice(
        f"This match has been tied {tie} times  so {score} points have been removed from this match"
    )
    if compScore == userScore:
        voice(
            f"We both have equal score so this match is tied: Boss your score is{userScore} and my scoreis {compScore}"
        )
    elif compScore > userScore:
        byscore = compScore - userScore
        voice(
            f"My score is higher than yours so you lose this match by {byscore}points : my score is {compScore} and your score is {userScore}"
        )

    elif compScore > userScore:
        byscore = userScore - compScore
        voice(
            f"Your score is higher than my score so you win this match by {byscore} : my score is {compScore} and your score {userScore}"
        )


if __name__ == "__main__":
    while True:
        a = takeComand().lower()
        if "play game" in a:
            rockPaperScissor()
            Voice("To play  this game again say 'play game' and to exit say 'exit'")
        elif "exit" in a:
            Voice("Game exited")
            exit()
