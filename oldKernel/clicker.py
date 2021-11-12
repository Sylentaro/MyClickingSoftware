import ctypes
import time
import keyboard

# PROGRAM_RUNNING = False
PROGRAM_PAUSED = True
# UPDATE_CAP = 1.0/60.0


# presses 'Key' for Time' seconds and then releases 'Key' and waits 'Time' seconds.
def press(Key='z', Time=0.05):
    # keyboard.write('The quick brown fox jumps over the lazy dog.')
    keyboard.press(Key)
    # keyboard.press('3')
    time.sleep(Time)
    keyboard.release(Key)
    # keyboard.release('3')
    time.sleep(Time)

# def main():
#     while True:
#         global PROGRAM_PAUSED
#         # if program paused...
#         if PROGRAM_PAUSED:
#             time.sleep(0.1)
#             if keyboard.is_pressed("page up"):
#                 PROGRAM_PAUSED = False
#                 print("Program unpaused - pressing buttons...")
#         # if program unpaused...
#         elif not PROGRAM_PAUSED:
#             press('z', 0.01)
#             if keyboard.is_pressed("page down"):
#                 PROGRAM_PAUSED = True
#                 print("Program paused - stopped pressing buttons...")


def main():
    while True:
        global PROGRAM_PAUSED
        # if program paused...
        if PROGRAM_PAUSED:
            time.sleep(0.1)
            if keyboard.is_pressed("page up"):
                PROGRAM_PAUSED = False
                print("Program unpaused - pressing buttons...")
        # if program unpaused...
        elif not PROGRAM_PAUSED:
            press(Key='z', Time=0.01)
            if keyboard.is_pressed("page down"):
                PROGRAM_PAUSED = True
                print("Program paused - stopped pressing buttons...")

# def engine():
#     global PROGRAM_RUNNING
#     global UPDATE_CAP
#
#     PROGRAM_RUNNING = True
#
#     render = False
#     firstTime = 0
#     lastTime = time.time()
#     delta = 0
#     unprocessedTime = 0
#
#     frameTime = 0
#     frames = 0
#     fps = 0
#
#     while PROGRAM_RUNNING:
#         render = False
#         firstTime = time.time()
#         delta = firstTime - lastTime
#         lastTime = firstTime
#
#         unprocessedTime += delta
#         frameTime += delta
#         while unprocessedTime >= UPDATE_CAP:
#             unprocessedTime -= UPDATE_CAP
#             render = True
#             if frameTime >= 1.0:
#                 frameTime = 0
#                 fps = frames
#                 frames = 0
#                 print(fps)
#         if render:
#             frames += 1
#         else:
#             time.sleep(1)


# print(datetime.now())
# current_frame = datetime.now() - timedelta(days=time_now.day, hours=time_now.hour, minutes=time_now.minute,
#                                            seconds=time_now.second, milliseconds=time_now.microsecond)
# delta = current_frame.microsecond


ctypes.windll.kernel32.SetConsoleTitleW("Button Clicker by Sylent")
print("Button Clicker - PAGE UP/DOWN to turn ON/OFF")
main()
