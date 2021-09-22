import scriptforgui as s, _thread, tkinter, time
import os
path = os.path.abspath(os.path.dirname(__file__))

#open default csv titled def.csv
try: s.commands = s.openCsv('def.csv')
except: 
    print('ERROR: failed to open default def.csv. Select file before Go Time.')
    s.changeCsvInput = False

def goTime():
    print('Starting macro.')
    s.keyPressed = False
    s.runningScript = True
    s.closeProgram = False
    s.changeCsvInput = False
    _thread.start_new_thread(s.input_thread, ())

def changeScript():
    s.changeCsvInput = True
    print('Changing script.')
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
        temp = temp + s.hotkeys[1] + ' to turn it off.'
        return temp
    else: 
        temp = "Macro isn't running.  Press "
        temp = temp + s.hotkeys[0] + ' to turn it on.'
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
            statuslbl.config(text = '')
        if(s.changeScriptEvent):
            s.changeScriptEvent = False
            changeScript()
            print('script should be changed')
        top.after(100, backgroundTask)
    except:
        print('Waiting for something to do.')
        top.after(1000, backgroundTask)
 
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
top.title('Scripto Thingy')
top.geometry('280x250')
go = tkinter.Button(top, text = "Run Script", command = goTime, width = 10)
change = tkinter.Button(top,text="Change Script",command = changeScript)
listbox = tkinter.Listbox(top)
listbox.place(x=110,y=50)
go.place(x=0,y=50)
change.place(x=0,y=80)
statuslbl = tkinter.Label(top)
statuslbl.pack()
selectedScriptLbl = tkinter.Label(top)
selectedScriptLbl.pack()
top.after(500, onStartUp)
top.mainloop()
s.closeProgram = True
