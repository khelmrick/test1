import datetime
import time

while True:
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Format the date and time as a string
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted date and time
    print("Keith-Current Date and Time:", formatted_datetime)

    # Wait for 5 seconds
    time.sleep(5)
