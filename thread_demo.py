import threading
import time


print('Start of program.')

def take_a_nap():
    time.sleep(5)
    print('Wake up!')


thred_obj = threading.Thread(target=take_a_nap)
thred_obj.start()
print('End of program.')
