from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")

speak.Speak("harry is a good boy")

speak.Speak("Raj somehow you did it best among the best coders of khaga")