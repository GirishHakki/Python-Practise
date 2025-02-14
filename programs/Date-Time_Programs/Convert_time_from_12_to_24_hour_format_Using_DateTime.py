from datetime import datetime

def convert24(time):
    # Parse the time string into a datetime object
    t = datetime.strptime(time, '%I:%M:%S %p')
    # Format the datetime object into a 24-hour time string
    return t.strftime('%H:%M:%S')

print(convert24('11:21:30 PM'))
print(convert24('12:12:20 AM'))
