from datetime import datetime
from datetime import timedelta

# from datetime import date


print("Pomodoro Timer")
task = input("What task are you working on? ")

workTime = timedelta(minutes=25)
breakTime = timedelta(minutes=5)
longBreakTime = timedelta(minutes=30)
currentTime = datetime.today()

times = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth"]
count = 0
lastTime = currentTime + workTime

print(f"Start time for {task} is {currentTime} :")
print()

for periods in times:

    print(f"End of {periods} study period is {lastTime.time()}")
    count += 1
    if count != 4:
        print(f"Next study period starts at {(lastTime + breakTime).time()}")
        lastTime = lastTime + breakTime
    else:
        print(f"Next study period starts at {(lastTime + longBreakTime).time()}")
        lastTime = lastTime + longBreakTime

    print()
