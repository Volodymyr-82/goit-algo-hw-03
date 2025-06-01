import random

def get_numbers_ticket(min, max, quantity):
    if min>max:
        print("Помилка: мінімум більший за максимум.")
        return []
    elif quantity > (max- min+ 1):
        print("Помилка: запрошено більше унікальних чисел, ніж можливо.")
        return []
    else:
      lottery_numbers=random.sample(range(min, max + 1), quantity)
      lottery_numbers.sort()
      return lottery_numbers
lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)
