import threading
import time


def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)


def brew_coffee():
    for i in range(1, 4):
        print(f"Brewing coffee for #{i}")
        time.sleep(3)


# create threads
order_thread = threading.Thread(target=take_orders)
brewing_thread = threading.Thread(target=brew_coffee)

order_thread.start()
brewing_thread.start()

# wait for both to finish
order_thread.join()
brewing_thread.join()
