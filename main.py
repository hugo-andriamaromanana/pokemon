from display import *
from pygameKEYS import *

if __name__ == "__main__":

    running = True

    while running:

        events = pygame.event.get()
        display_PKMN_info()

        for event in events:
            running = ESC_KEYDOWN(event)

        pygame.display.update()
