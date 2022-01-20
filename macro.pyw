import macro2 as s, _thread, tkinter, time, os
path = os.path.abspath(os.path.dirname(__file__))

#open default csv titled def.csv
try: s.commands = s.openCsv('def.csv')
except: 
    print('ERROR: failed to open default def.csv. Select file before Go Time.')
    s.changeCsvInput = False
    
def goTime():
    #killing old threads
    s.closeProgram = True
    time.sleep(0.01)
    #starting new thread
    print('Starting macro.')
    _thread.start_new_thread(s.input_thread, ())
    
def changeScript():
    s.changeCsvInput = True
    print('Changing macro.')
    s.files, printThis = s.listFiles(path)
    s.runningScript = False
    s.closeProgram = True
    print('starting new next key thread')
    _thread.start_new_thread(s.nextKey_thread, ())
    print('updating list box')
    listbox.delete(0, tkinter.END)#this line is causing problems when using the home key to call this method
    for i in range(len(printThis)):
        listbox.insert(i, printThis[i])
    print('waiting for next key input')
    refreshLabels()
    goTime()
    
def isMacroRunningText():
    if(s.runningScript): 
        temp = 'Macro is running.  Press '
        temp = temp + str(s.settings[1]) + ' to turn it off.'
        return temp
    else: 
        temp = "Macro isn't running.  Press "
        temp = temp + str(s.settings[0]) + ' to turn it on.'
        return temp
    
def refreshLabels():
    s.updateScriptLbl = True
    while(s.updateScriptLbl):
        time.sleep(0.4)
        textis = 'Macro Loaded: ' + s.csvRunning
        selectedScriptLbl.config(text = textis)
        top.update_idletasks()
        
def backgroundTask():
    try:
        if(not s.closeProgram):
            statuslbl.config(text = isMacroRunningText())
            top.update_idletasks()
        else:
            statuslbl.config(text = 'Script disabled.')
        if(s.changeScriptEvent):
            s.changeScriptEvent = False
            changeScript()
            print('Macro should be changed')
        top.after(100, backgroundTask)
    except:
        print('Waiting for something to do.')
        top.after(1000, backgroundTask)
        
def viewCommands():
    commandsWindow = tkinter.Tk()
    commandsWindow.title('Macro Commands')
    commandsWindow.geometry('200x250')
    commandsList = tkinter.Listbox(commandsWindow, width = 30, height = 20)
    tempStr = 'Macro running: ' + s.csvRunning
    commandsList.pack()
    commandsList.insert(0,"i'm aware that this looks terrible. fight me.")
    commandsList.insert(1,tempStr)
    commandsList.insert(2,'Inputs  On Press  On Release')
    for i in range(len(s.commands)):
        command = s.commands[i]
        commandsList.insert(i+3,command.keyIn+'          '+command.onPress+'             '+command.onRelease)
    
def onStartUp():
    goTime()
    time.sleep(0.01)
    textis = 'Macro Loaded: ' + s.csvRunning
    selectedScriptLbl.config(text = textis)
    top.update_idletasks()
    try:
        s.files, printThis = s.listFiles(path)
        for i in range(len(printThis)):
            listbox.insert(i, printThis[i])
        top.after(0, backgroundTask)
    except:
        print('error with set up')
        top.after(1000, onStartUp)
        
#gui things
top = tkinter.Tk()
top.title('Macro Thingy')
top.geometry('300x250')
go = tkinter.Button(top, text = "Run Macro", command = goTime, width = 10)
change = tkinter.Button(top,text="Change Macro",command = changeScript)
listbox = tkinter.Listbox(top)
listbox.place(x=110,y=50)
go.place(x=0,y=50)
change.place(x=0,y=80)
viewCommands = tkinter.Button(top,text="View Macro",command = viewCommands)
viewCommands.place(x=0,y=110)
statuslbl = tkinter.Label(top)
statuslbl.pack()
selectedScriptLbl = tkinter.Label(top)
selectedScriptLbl.pack()

#start things
top.after(0, onStartUp)
top.mainloop()
s.closeProgram = True
