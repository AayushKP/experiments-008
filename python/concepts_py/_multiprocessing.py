import time
from multiprocessing import Process


def brew_coffee(name):
    print(f"{name} coffee brewing")
    time.sleep(3)
    print(f"End of {name} coffee brewing")


if __name__ == "__main__":
    coffee_makers = [
        Process(target=brew_coffee, args=(f"Coffee Maker #{i + 1}",)) for i in range(3)
    ]

    # Start all process
    for p in coffee_makers:
        p.start()

    # wait for all to complete
    for p in coffee_makers:
        p.join()

    print("All coffee served")
