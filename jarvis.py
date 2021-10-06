import pyttsx3
import speech_recognition as sr
import datetime
import os

import wikipedia
from playsound import playsound
import webbrowser
import smtplib



engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

# speaks whatever audio is given to 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning swayam ! have a great day ahead")
    
    elif hour>=12 and hour<=18:
        speak("good after noon sir !")
    else:
        speak("good evening swayam . i hope your day well spent .")

    # speak("please tell me how may i help you ? ")


# taking input through microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        r.energy_threshold=1000
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n") 
        
    
    except Exception as e:
        print(e)
        print("say that again please ....") 
        return "None"
    return query
       


def chat(query):
    if "thank you" in query:
        speak("you are most welcome sir.")

    elif "hello jarvis" in query or "hey jarvis" in query or query=="jarvis" or query=="hello":
        speak("yes sir ...")

    elif "the time" in query:
        time=datetime.datetime.now().strftime("%H:%M:%S")   
        print(time)
        speak(f"sir, the time is {time}" )
    
    elif "who is swayam" in query:
        speak("swayam is creator. apparently he is my god. the  guy who never think to give up is swayam.")
    
    elif "repeat me" in query:
        speak("please say something")
        rep=takeCommand().lower()
        speak(rep)



def action(query):
    if "open youtube" in query:
        webbrowser.open("youtube.com")


    elif "open google" in query:
        webbrowser.open("google.com")


    elif "play song" in query:
        music_dir=("C:\\Users\DELL\Music\Favourite")
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

        
    elif "open code" in query:
        os.startfile("C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    



def sendEmail(to,content):
     server=smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('swayamprakash97691@gmail.com','#ironman*')
     server.sendmail('swayamprakash97691@gmail.com',to,content)
     server.close()

if __name__ == '__main__':
#   speak(" namaskar . apana mane khusi ta ? ")
    wishMe()
    while True:
        query=takeCommand().lower()

        chat(query)
        action(query)
        if 'wikipedia' in query:
            speak("searching to wikipedia...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia ")
            speak(result)
        
        
        elif "Bye" in query or "bye" in query or "By" in query or "by" in query:
            speak("Glad to help you sir . good bye .")
            break
        

        elif "send email" in query:
            try:
                speak("what should i send?")
                content=takeCommand()
                to="nmbaibhab@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            
            except Exception as e:
                print(e)
                speak("sorry , i could not send the message")
    

        


        

        
          
         

         

        


        
        
        

            
             
           