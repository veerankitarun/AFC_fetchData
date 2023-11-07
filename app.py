import time
import board
import adafruit_memsmic

# Define the I2S microphone and configure it
mic = adafruit_memsmic.MEMS_I2S(12_000_000)  # Adjust the sample rate if needed

# Main loop to read data
while True:
    audio_data = mic.record(1024)  # Read 1024 audio samples
    print(audio_data)
    time.sleep(0.1)  # Add a delay to control the data rate
