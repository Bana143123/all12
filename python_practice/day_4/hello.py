import hi
import time
import importlib
hi.say()
time.sleep(10)# here within 10 seconds im trying to change the script so that it takes the updated script by using importlib.reload module without rerun the code
importlib.reload(hi)
hi.say()