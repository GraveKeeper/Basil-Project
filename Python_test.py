# Initial print to check run in console
print("Program Runs")

import time 
from datetime import datetime
# Python Timer Test
def main():
   
    Test = time.time()
    timestamp = Test
    dt_object = datetime.fromtimestamp(timestamp)

    print("dt_object = " , dt_object)
    print("type(dt_object) = ", type(dt_object))
if __name__ == "__main__":
   main()

