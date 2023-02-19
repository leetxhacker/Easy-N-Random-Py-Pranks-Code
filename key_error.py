import sys
import time
# <------- LeeTxHacker ------->
print("Press Ctrl + C If You Want To Exit")

while True:
    try:
        print("Keyboard Interrupted\n")
        time.sleep(1)
    except KeyboardInterrupt:
        print("[+] Program Stopped")
        sys.exit()
