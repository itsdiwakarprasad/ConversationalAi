print(">> A.I. is starting please wait.....")
from Brain.AIBrain import ReplyBrain
from Brain.QnA import QuestionsAnswer
from Body.Listen import MicExecution
from Body.Speak import Speak
from Features.Clap import Tester
print(">> All set, A.I. is Activating.....")

def MainExecution():

    Speak("Hello Sir")
    Speak("I'm Ready.")

    while True:

        Data = MicExecution()
        Data = str(Data)

        if len(Data)<3:
            pass

        elif "when" in Data or "how much" in Data or "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            Speak(Reply)

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
        MainExecution()
    else:
        pass

print("Clap to Start")
ClapDetect()

# 10% 