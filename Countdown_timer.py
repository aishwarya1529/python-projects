import time
my_time = int(input("enter the time in seconds"))

for x in range(my_time,0,-1): # for counting backwards
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x / 3600)
    print(f"00:{minutes:02}:{seconds:02}")  # '02',2-as we want 2 digits to display in sec and 0- from 1 to 9 it will be 01,02...
    time.sleep(1)

print("TIME'S UP!!")
