import mouse
import time
import keyboard


def punch(punches):
    """
    This function changes the amount of times you punch
    punches: number (integer) of punches thrown
    Note: Modify punches based upon your stamina
    """
    for i in range(0, punches + 1):
        mouse.click('left')
        time.sleep(0.5)
        mouse.click('left')
        time.sleep(0.5)


# give time to kick off
time.sleep(5)

# starting time
start = time.time()

counter = 0

while counter <= 150:
    punch(5)
    print("Clicked: ", counter)

    counter += 1

    # pause to regain stamina
    time.sleep(8)

    # move forward in case punches send you backwards
    keyboard.press("w")
    keyboard.release("w")

# ending time
end = time.time()

print(f"Runtime of the program is {end - start}")
print("Program ended")
