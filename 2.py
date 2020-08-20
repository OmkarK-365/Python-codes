
#import pyttsx3
import os

#pyttsx3.speak("Welcome to Windows Tools!")
#pyttsx3.speak("Myself Win Assistant!")

options_list=["Basic Windows Apps List:" , "1.Browser(Chrome,Edge,Firefox,etc)" , "2.Windows Media Player" , "3.ShutDown or Restart the Computer" , "4.Open Snipping Tool" , "5.Control Panel" , "6.Command Prompt" , "7.Calcultor" , "8.PowerShell" , "9.Screen Magnifier" , "10.Narrator" , "11.On Screen KeyBoard" , "12.Microsoft Paint" , "13.Computer Management" , "14.Task Manager" , "15.Unziper"]

while True:
    print("..................................................................................................")
    print("This is a Virtual Assistant named 'WinAssistant'. You can use this to run your basic Windows Apps.")
    print("Instructions:")
    print("1.Type in sentences.")
    print("2.To exit type 'exit'")
    print("3.Type in lower case")
    print("4.To see Available Options Type 'options'")
    print("Chat With Me with ur requirement:" , end='')
    p = input()
        
    if ("options" in p ):
        print(options_list[0])
        print(options_list[1])
        print(options_list[2])
        print(options_list[3])
        print(options_list[4])
        print(options_list[5])
        print(options_list[6])
        print(options_list[7])
        print(options_list[8])
        print(options_list[9])
        print(options_list[10])
        print(options_list[11])
        print(options_list[12])
        print(options_list[13])
        print(options_list[14])
        print(options_list[15])  
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("chrome" in p) or ("browser" in p) or ("edge" in p) or ("firefox" in p)):
        if ("chrome" in p):
            os.system("start chrome")
            print("Opening Chrome Browser")
        elif("browser" in p):                                                                    #"start chrome " is used bcuz in every device path is not set!
            os.system("start iexplore")
            print("Opening Browser")
        elif ("edge" in p):
            os.system("start msedge")
            print("Opening Edge Browser")
        elif ("firefox" in p):
            os.system("start firefox")
            print("Opening Mozilla Firefox")
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("files" in p) or ("explorer" in p) or ("this pc" in p) or ("file explorer" in p)):
        if ("files" in p):
            os.system("start explorer")
            print("Opening Files")
        elif ("explorer" in p):
            os.system("start explorer")
            print("Opening Explorer")
        elif ("this pc" in p):
            os.system("start explorer")
            print("Opening This PC")
        elif ("file explorer" in p):
            os.system("start explorer")
            print("Opening File Explorer")
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("notepad" in p) or ("text editor" in p)):
        if ("notepad" in p):
            os.system("start notepad")
            print("Opening Notepad")
        elif ("text editor" in p):
            os.system("start notepad")
            print("Opening Text Editor")
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("cmd" in p) or ("command line" in p) or ("cli" in p) or ("command prompt" in p)):  
        if ("cmd" in p):
            os.system("start cmd")
            print("Opening CMD")
        elif ("command line" in p):
            os.system("start cmd")
            print("Opening Command Line")
        elif ("cli" in p):
            os.system("start cmd")
            print("Opening CLI")
        elif ("command prompt" in p):
            os.system("start cmd")  
            print("Opening Command Prompt")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("taskmanager" in p) or ("processes" in p) or ("task manager" in p) or ("taskmgr")):    
        if ("taskmanager" in p):
            os.system("start Taskmgr")
            print("Opening Task Manager")
        elif ("processes" in p):
            os.system("start Taskmgr")
            print("Opening Processes")
        elif ("task manager" in p):
            os.system("start Taskmgr")
            print("Opening Task Manager")
        elif ("taskmgr" in p):
            os.system("start Taskmgr")
            print("Opening Task Manager")
    
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("paint" in p) or ("whiteboard" in p) or ("microsoft paint" in p) or ("mspaint" in p)): 
        if ("paint" in p):
            os.system("start mspaint")
            print("Opening Paint")
        elif ("whiteboard" in p):
            os.system("start mspaint")
            print("Opening Whiteboard")
        elif ("microsoft paint" in p):
            os.system("start mspaint")
            print("Opening Microsoft Paint")
        elif ("mspaint" in p):
            os.system("start mspaint")
            print("Opening Microsoft Paint")
        
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("osk" in p) or ("on screen keyboard" in p) or ("keyboard" in p)):  
        if ("osk" in p):
            os.system("start osk")
            print("Opening On Screen Keyboard")
        elif ("on screen keyboard" in p):
            os.system("start osk")
            print("Opening On Screen Keyboard")
        elif ("keyboard" in p):
            os.system("start osk")
            print("Opening On Screen Keyboard")
    
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("calc" in p) or ("calculator" in p)):  
        if ("calc" in p):
            os.system("start calc")
            print("Opening Calculator")
        elif ("calculator" in p):
            os.system("start calc")
            print("Opening On Screen Keyboard")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("media player" in p) or ("windows media player" in p) or ("music player" in p) or ("video player" in p) or ("wmplayer" in p)): 
        if ("media player" in p):
            os.system("start wmplayer")
            print("Opening Media Player")
        elif ("windows media player" in p):
            os.system("start wmplayer")
            print("Opening Windows Media Player")
        elif ("music player" in p):
            os.system("start wmplayer")
            print("Opening Music Player")
        elif ("video player" in p):
            os.system("start wmplayer")
            print("Opening Video Player")
        elif ("wmplayer" in p):
            os.system("start wmplayer")
            print("Opening Windows Media Player")
        
    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("snip tool" in p) or ("snipping tool" in p) or ("screen snip" in p) or ("snippingtool" in p)): 
        if ("snip tool" in p):
            os.system("start snippingtool")
            print("Opening Snip Tool")
        elif ("snipping tool" in p):
            os.system("start snippingtool")
            print("Opening Snipping Tool")
        elif ("screen snip" in p):
            os.system("start snippingtool")
            print("Opening Screen Snip")
        elif ("snippingtool" in p):
            os.system("start snippingtool")
            print("Opening Snipping Tool")  

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("control panel" in p) or ("control" in p)):    
        if ("control panel" in p):
            os.system("start control")
            print("Opening Control Panel")
        elif ("control" in p):
            os.system("start control")
            print("Opening Control")

    elif (("run" in p) or ("open" in p) or ("execute" in p) or ("start" in p)) and (("computer management" in p) or ("compmgmt" in p) or ("computer manager" in p)):    
        if ("computer management" in p):
            os.system("start compmgmt")
            print("Opening Computer Management")
        elif ("compmgmt" in p):
            os.system("start compmgmt")
            print("Opening Computer Management")
        elif ("computer manager" in p):
            os.system("start compmgmt")
            print("Opening Computer Manager")
        

    elif("exit" in p):
        print("Thank You For Using!!")
        print("Exiting.....")
        break
    else:
        print("Not Supported!")
        




