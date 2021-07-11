# Macro-Manager-With-Gui
erp is required


This is ugly, but it's functional.

IMPORTANT: run as administrator or it won't work for TERA!

# INFO

Supports both automated keyboard presses and automated mouse clicks. Doesn't detect your mouse clicks yet - 
this could be added in the future if I decide it's worthwhile.
Press the "Go Time" button to turn on the script with the macro enabled, otherwise the gui will just run on its own in the background.
Macro is enabled when you press "enter-r-enter."
Also enables when you press "/p r enter." So if you change to party chat and type r, it'll think you're ready.
It disables off when you press enter.
Other commands for turning it on/off are on settings.csv.
The macros are edited on def.csv. Other macros can be added by you creating your own .csv files.
The code is designed to easily switch between multiple macros, so go ahead and make up to 10 of them and have fun.
Editing the macros on excel is not advised because it'll try to autoformat - and you don't want that. Use notepad.

Note: these are .csv files, which stands for "comma separated values." They are divided into three 
columns that the code reads from. Each column is separated by a comma. Every line in the file must
have at least two commas in it, making three or more columns. The fourth column or any more after the
third column will be unread by the code and can be used for making any comments you want.

Formatting for the leftmost column (inputs):
Only one key can be used for each line.
Regular keys should be in '' or "".
Special keys should have Key. typed out, followed by the key. Such as Key.shift or Key.f5. They can't be in '' or "".

Formatting for the second (on_press) and third columns (on_release):
The second column keys are instantly pressed by the machine as soon as you press the input key associated with them.
The third column keys are instantly pressed by the machine as soon as you let go of the input key associated with them.
Regular keys or groups of keys are just typed out normally.
Special keys need to be inside {} like {tab} or {f8}.
Waits can be added also inside {}. {0.05} will tell the code to wait 0.05 seconds before pressing the keys after it.
Multiple keys can be pressed at the same time using <>. <{shift}f> will press shift+f (so, a capital F).
Mouse clicks can be added inside (). r = right click and l = left click. So (rl) is right click then left click.

TERA players send gold to Crooow on Velika NA.

# FOR THOSE WHO WISH TO RUN THE .PY INSTEAD OF THE .EXE
Have Python installed, yada yada hoohaw, whatever. Run the guistuff.py, not the scriptforgui.py. Have both the .py in the same folder though, of course. Make sure you've got all the neccesarrily imports listed at the top of the files.
