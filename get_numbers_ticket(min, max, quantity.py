import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers=[]
    while len(lottery_numbers)<quantity:
        num=random.randint(min, max)
        lottery_numbers.append(num)
    return lottery_numbers
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)
