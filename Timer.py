import time 

t = int(input("Enter the time in seconds:\n"))

while t:
    min = t // 60
    sec = t % 60
    timer = '{:02d}:{:02d}'.format(min, sec)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

print("Time is out!")