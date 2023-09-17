# for windows
# Start by importing the win32com package
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
names = ["Zain", "Bilal", "Javed", "Asjid", "John", "Harry Potter"]
for name in names:
 speak.Speak(f" Shoutout to{names}")