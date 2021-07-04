import scriptforgui as s, _thread, tkinter, time
import os
path = os.path.abspath(os.path.dirname(__file__))

#open default csv titled def.csv
try: s.commands = s.openCsv('def.csv')
except: 
    print('ERROR: failed to open default def.csv. Select file before Go Time.')
    s.changeCsvInput = False

def goTime():
    s.keyPressed = False
    s.runningScript = True
    s.closeProgram = False
    s.changeCsvInput = False
    _thread.start_new_thread(s.input_thread, ())
    while(s.closeProgram == False):
        time.sleep(0.5)
        statuslbl.config(text = isMacroRunningText())
        top.update_idletasks()
    statuslbl.config(text = '')

def changeScript():
    s.files, printThis = s.listFiles(path)
    s.runningScript = False
    s.changeCsvInput = True
    _thread.start_new_thread(s.nextKey_thread, ())
    listbox.delete(0, tkinter.END)
    for i in range(len(printThis)):
        listbox.insert(i, printThis[i])
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
        time.sleep(0.5)
        textis = 'Macro Loaded: ' + s.csvRunning
        selectedScriptLbl.config(text = textis)
        top.update_idletasks()
    
#gui things
top = tkinter.Tk()
top.title('Scripto Thingy')
top.geometry('280x250')
go = tkinter.Button(top, text = "Go Time", command = goTime, width = 10)
change = tkinter.Button(top,text="Change Script",command = changeScript)
listbox = tkinter.Listbox(top)
listbox.place(x=110,y=50)
go.place(x=0,y=50)
change.place(x=0,y=80)
statuslbl = tkinter.Label(top)
statuslbl.pack()
selectedScriptLbl = tkinter.Label(top)
selectedScriptLbl.pack()
top.mainloop()
s.closeProgram = True
