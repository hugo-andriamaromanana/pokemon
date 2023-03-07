from display import *
from pygameKEYS import *

runnning= True

while runnning:
    display_PKMN_info()
    events= pygame.event.get()
    for event in events:
        running=ESC_key_pressed(events)