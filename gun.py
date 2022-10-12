import numpy as np
# assume all bullets hit on body
class Gun:
    def __init__(self, name, magsize, range_vec, dpb, firerate, reload_speed) -> None:
        # static variables 
        self.name = name
        self.magazine_size = magsize
        self.effective_range_vector = range_vec

        self.dpb = dpb # damage per bullet
        self.firerate = firerate # per second
        self.reload_speed = reload_speed # in seconds

    


if __name__ == "__main__":
    mfour = Gun("m4a1", 30, [85, 65, 20], 30, 13, 1)
    sniper = Gun("intervention", 5, [100, 90, 80], 120, 0.7, 2)



