import time
import winsound

# Set the interval (in seconds) for the sound to occur. 45 minutes = 2700 seconds
interval = 2700

while True:
    # Wait for the specified interval
    time.sleep(interval)
    # Play a beep sound with a frequency of 1000 Hz for 1 second
    winsound.Beep(1000, 1000)
