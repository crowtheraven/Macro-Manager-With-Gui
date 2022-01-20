from pynput.keyboard import Controller as keyboard, Listener, Key

#Keys
toggleOn = Key.page_up
toggleOff = Key.page_up
close = Key.ctrl_r
change = Key.home

#string
readyCheck = '{f8}{0.25}<{ctrl}c>{0.45}<{ctrl}x>'
defaultMacro = 'def.txt'

#True or False
sound = True
enterDisablesMacro = True
