import os 
files = os.listdir("F:/Quran Client/Footage/New")
i  =252
for file in files:
        os.rename(f"F:/Quran Client/Footage/New/{file}", f"F:/Quran Client/Footage/New/{i}.mp4")
        i = i +1
