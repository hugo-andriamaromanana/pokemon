from pygameKEYS import *

def reset_pokemon():
    global random_pokemon
    ID= choice(range(GENERATION[gen][0], GENERATION[gen][1]))
    random_pokemon= Pokemon(ID, False).get_attributes()

if __name__ == "__main__":

    running = True
    ID= choice(range(GENERATION[gen][0], GENERATION[gen][1]))
    random_pokemon= Pokemon(ID, False).get_attributes() 

    while running:

        events = pygame.event.get()

        display_PKMN_info(random_pokemon)
        for event in events:
            running = ESC_KEYDOWN(event)
            if NEXT_PKMN_KEYDOWN(event):
                reset_pokemon()
        pygame.display.update()
