import numpy as np
import time
import random
# assume all bullets hit on body
class Gun:
    def __init__(self, name, magsize, range_vec, dpb, firerate, reload_speed) -> None:
        # static variables 
        self.name = name
        self.magazine_size = magsize
        self.effective_range_vector = range_vec

        self.dpb = dpb # damage per bullet
        self.firerate = firerate # bullets fired PER ITERATION
        self.reload_speed = reload_speed # in seconds

    def simulate(self):
        t_end = time.time() + 60
        while time.time() < t_end:
            self.shoot()
        return

    def shoot(self, acc:int, bullets_in_mag:int):
        if random.randint(100) <= acc:
            # calculate damage done
            if bullets_in_mag == 0:
                time.sleep(self.reload_speed)
            else:
                return self.dpb * self.firerate # calculate how many bullets have been shot ROUND UP
        else:
            return 0

if __name__ == "__main__":
    mfour = Gun("m4a1", 30, [85, 65, 20], 30, 13, 1)
    sniper = Gun("intervention", 5, [100, 90, 80], 120, 0.7, 2)



