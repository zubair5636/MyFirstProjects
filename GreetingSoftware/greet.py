# This script greets the user based on the current time of day.
from time import strftime
from pyttsx3 import speak

timestamp = strftime("%H:%M:%S")


#morning
mo1= ("Good Morning Sir! Sir the time is")
mo2 = ("May You will have a good day")
mo3= (mo1,timestamp,mo2)

#afternoon
af1= ("Good Afternoon Sir! sir the time is")
af2= ("You should take the lunch!")
af3= (af1,timestamp,af2)

#evening
ev1= ("Good Evening Sir! Sir the time is")
ev2= ("Hope You had a good day.  Now it's time to take a sleep")
ev3= (ev1,timestamp,ev2)


if (timestamp < "12:00:00"):
    speak(mo3)

elif (timestamp < "18:00:00"):
    speak(af3)

else:
    speak(ev3)
