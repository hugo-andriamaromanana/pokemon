from pygame.locals import *

def ESC_key_pressed(events):
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
    return True

def BACKSPACE_key_pressed(events):
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                return True
    return False

def ENTER_key_pressed(events):
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                return True
    return False

def UP_key_pressed(events):
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_UP:
                return True
    return False

def DOWN_key_pressed(events):
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                return True
    return False

def BUTTON_pressed(events, button):
    for event in events:
        if event.type == MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                return True
    return False