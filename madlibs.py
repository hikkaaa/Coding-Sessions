from sample_madlibs import hp, coding, zombie, sad_banana, mycrash
import random

if __name__ == "__main__":
    m = random.choice([hp, coding, zombie, sad_banana, mycrash])
    m.madlib()