import time
my_time=int(input("enter time in minutes: "))
time_in_seconds=int(my_time*60)

for x in range(time_in_seconds,0,-1):
    seconds=int(x%60)
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("time's up!")