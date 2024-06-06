from src.utils.api import API
from src.utils.client import Client

import threading
import time

def main():
    # Virtual limitation of 2 clients at a time (buying, reserving, releasing)
    semaphore = threading.Semaphore(2)

    for i in range(1, 11):
        client = Client(i, semaphore)
        threading.Thread(target=client.run).start()
        time.sleep(1)

if __name__ == "__main__":
    main()