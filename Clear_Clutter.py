import os
files = os.listdir("Clutterd_Folder")
i = 1 # means i ki inital value 1 ha.
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"Clutterd_Folder/{file}", f"Clutterd_Folder/{i}.jpg")
        i = i +1