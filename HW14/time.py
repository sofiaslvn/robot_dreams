from weather_threads import result
from weather_multiprocessing import result2

if result > result2:
    print("threads slower")
else:
    print("multiprocess slower")