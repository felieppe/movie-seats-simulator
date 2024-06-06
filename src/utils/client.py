import random
import time

from src.utils.api import API

class Client:
    def __init__(self, id, semaphore):
        self.id = id
        self.semaphore = semaphore
        self.api = api = API("http://localhost:3000", {"Content-Type": "application/json"})

    def choose_random_seat(self, max):
        return random.randint(1, max)

    def reserve_seat(self, seat):
        self.semaphore.acquire()

        response = self.api.reserve_seat_by_id(seat, {"client": self.id})
        return response["success"]

    def buy_seat_rng(self, seat):
        if (random.random() < 0.5):
            time.sleep(random.uniform(1, 2))
            response = self.api.book_seat_by_id(seat, {"client": self.id})
            return response["success"]
        else:
            time.sleep(random.uniform(1, 10))
            self.api.release_seat_by_id(seat, {"client": self.id})
            
            self.semaphore.release()
            return False

    def run(self):
        while(True):
            seat = self.choose_random_seat(80)
            print(f"Client {self.id} randomly chose seat {seat}.")
            if self.reserve_seat(seat):
                print(f"Client {self.id} reserved seat {seat}.")
                if self.buy_seat_rng(seat):
                    print(f"Client {self.id} bought seat {seat}.")
                    self.semaphore.release()
                else:
                    print(f"Client {self.id} failed to buy seat {seat}.")
                    self.semaphore.release()
            else:
                print(f"Client {self.id} failed to reserve seat {seat}.")

                self.semaphore.release()
                time.sleep(random.uniform(1, 5))
    