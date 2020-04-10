
import time 

def convert_time(sec):

	mins = sec // 60
	sec = sec % 60
	hours = mins // 60
	mins = mins % 60
	print("Time elapse: {0}:{1}:{2}".format(int(hours), int(mins), int(sec)))


start = input("Press enter to start timer:\n")

print("The timer has started")

begin = time.time()
 
input("Press enter to stop timer:\n")

stop = time.time()

time = stop - begin

convert_time(time)
