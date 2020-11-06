import keyboard
import webbrowser
import time
#it's recomended to save the java program as a txt file without the tabs ,{},() and then add them later in the VPL
#open the file
f = open("code.txt", "r")
#read the file
file = f.read()
#link of "Testat"
url = 'link to the Testat'

#open the Browser
webbrowser.open_new_tab(url)
#wait 10 seconds
time.sleep(10)
# type the program
for c in file:
    keyboard.write(c)
    #you can remove the sleep if you don't want to watch the program type it out
    time.sleep(0.2)
f.close()   

