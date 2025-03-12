import time
import random
import pygetwindow as gw
import pygame

OPEN_SOUNDS = ["trifileVic.wav", "impressive.wav", "malformed.wav", "huddled.wav", "madness.wav", "ritual.wav"]
CLOSE_SOUNDS = ["onslaught.wav", "overconfidence.wav", "moredust.wav", "sendthis.wav", "executed.wav", "twisted.wav"]



SOUND_PROB = 0.35
displayWindows = True

pygame.mixer.init()
if pygame.mixer.get_init() is None:
    print("\n\nAudio Dependencies failed to initalize, double check pygame installation or run 'pip install pygame' ")
else:
    print("\n\nAudio Dependencies offically initalized")

SOUND_PROB = int(input("\nHow often would you like to hear the narrator speak (ENTER IN PERCENTAGE)\n"))

if SOUND_PROB == 100:
    SOUND_PROB = 1.0
else: 
    SOUND_PROB = SOUND_PROB / 10

SOUND_VOL = int(input("\nHow loud do you want the narrator to be? (ENTER IN PERCENTAGE)\n"))

if SOUND_VOL == 100:
    SOUND_VOL = 1
else:
    SOUND_VOL = SOUND_VOL / 10

userAns = input("\nWould you like the console to log which windows have been opened? (Y/N)\n")

if userAns == "Y" or userAns == "y":
    displayWindows = True
else: 
    displayWindows = False




def get_open_windows():
    return set(gw.getAllTitles())

def play_sound(sound_file):
    try:
        sound = pygame.mixer.Sound(sound_file)
        sound.set_volume(SOUND_VOL)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing sound: {e}")

def get_random_sound(sound_list):
    return random.choice(sound_list)

def should_play_sound():
    return random.random() < SOUND_PROB

def monitor_windows():
    previous_windows = get_open_windows()

    while True:
        time.sleep(1)
        current_windows = get_open_windows()

        opened_windows = current_windows - previous_windows

        if opened_windows and displayWindows == True:
            print(f"opened window: {opened_windows}")

        if opened_windows:
            if should_play_sound():
                random_open_sound = get_random_sound(OPEN_SOUNDS)
                play_sound(random_open_sound)
        
        closed_windows = previous_windows - current_windows

        if closed_windows and displayWindows == True:
            print(f"Closed window: {closed_windows}")
        
        if closed_windows:
            
            if should_play_sound():
                random_close_sound = get_random_sound(CLOSE_SOUNDS)
                play_sound(random_close_sound)

        previous_windows = current_windows

if __name__ == "__main__":
    print("Narrator initialized...")
    monitor_windows()