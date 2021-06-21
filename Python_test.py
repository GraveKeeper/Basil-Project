# Initial print to check run in console
print("Program Runs")

import time , threading
from datetime import datetime

# Python Timer Test
def main():
   
    Test = time.time()
    timestamp = Test
    dt_object = datetime.fromtimestamp(timestamp)

    print("dt_object = " , dt_object)
main()

   
# Make timer that prints after () ammount of time.
def funtion(a):

    timer = threading.Timer(a, timer)
    timer.start()
    print("now keeping time!\n")
    timer.cancel()
    print("Exit Timer!\n")
    return