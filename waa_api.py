from datetime import datetime  
import pywhatkit

def send_msg(now):
     return pywhatkit.sendwhatmsg("+573194772672", "Hi", now.hour, now.minute+1)
    # pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png", "Hello")