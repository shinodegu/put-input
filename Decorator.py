from datetime import datetime
import time

def times(lead_time):
     start = time.time()
     lead_time()
     end = time.time() - start
     print(end)


@times
def number():
    for i in range(10000):
       print(i)

print("*"*50)

@times
def cubes():
    for z in range(300):
      z+=z**3
      print(z)

number()
cubes()

