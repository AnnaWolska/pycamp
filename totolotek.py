"""Program for counting how many times someone must play in totolotek to win it"""
import random

numbers = {1, 9, 11, 21, 7, 3}
all_possible_numbers = range(1, 50)
print(all_possible_numbers)

def drew_numbers():

    """Give random numbers for the totolotek game player
    """
    return set(random.sample(all_possible_numbers, k=6))
if __name__ == '__main__':

    counter = 0
    random_draw = {}
    while numbers != random_draw:
        random_draw = drew_numbers()
        counter += 1
        print(counter)

    total_cost = counter * 3
    total_time = counter / 365
    print(f"BRAWO WYGRANA po {counter} razach, wydałeś {total_cost:,} \
     złote, zajęło Ci to {total_time:,} lat")
