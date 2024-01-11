# get list file txt
print("+ Make sure your file's visibility "+'in Google Drive is set to "Anyone with the link"')
print("+ Time: 5 minus is 300s, 10 minus is 600s, 1 hour is 3600s, 1 day is 8640s,...")
# print("input file example test.txt")

import webbrowser
import time
import shutil
import os

# An input is requested and stored in a variable
# name = input ("Enter a name file text: ")
file_name = "google_drive_file_url.txt"

# input file name
file_name_loading = 'loading_' + file_name

# create file loading
if os.path.exists(file_name_loading):
    os.remove(file_name_loading)
    shutil.copy2(file_name, file_name_loading)
    # pass
else:
    shutil.copy2(file_name, file_name_loading)

number_second_text = input ("Enter a number seconds for open tab browser: ")

# Converts the string into a integer. If you need
# to convert the user input into decimal format,
# the float() function is used instead of int()
number_second = int(number_second_text)

# Prints in the console the variable as requested
print ("The number you entered is: ", number_second)

f = open(file_name_loading,'r')
urls = f.readlines()
for url in urls:
    print(url)
    with open(file_name_loading, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != url:
                f.write(i)
        f.truncate()
    url = url[32:]
    end = url.index('/')
    ID = url[:end]
    download_link = 'https://drive.google.com/uc?export=download&id='+ID
    webbrowser.open(download_link)
    # print('This Your Direct Download Link : ',download_link)

    time.sleep(number_second)
    

# clear 
import os
clear = lambda: os.system('cls')
clear()



