# application generates random numbers

import random
import sys
from time import sleep

def generate_num():
    print("Random number generated: {0}".format(random.randrange(999)))

if __name__ == "__main__":
    l = len(sys.argv)
    
    for arg in sys.argv:
        print(arg)

    generate_num()
