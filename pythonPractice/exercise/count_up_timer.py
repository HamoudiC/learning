# count up timer

import time

#end goes first because non default arguments go behind default arguments 
def count(end, start = 0 ):
    for x  in range (start,end+1):
        print(x)
        time.sleep(1)

    print("DONE!")

# since start = 0, I only need to enter the end argument
# If I want to start somewhere other than 0 I need to enter a start argument 
count(30,20)
