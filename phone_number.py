"""
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

"""
"""
Нормалізовані номери телефонів для SMS-розсилки: ['+380671234567', '+380952345678', 
'+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', 
'+380501112222', '+380501112211']

"""
def normalize_phone(phone_number):
    need_number=phone_number.strip()
    symbol_del=["-", "(", ")", " ","+"]
    for symbol in symbol_del:
      need_number=need_number.replace(symbol,"")
    if not need_number.startswith('38'):
      need_number="38"+ need_number
    return "+" + need_number
print(normalize_phone("    38050-111-22-22"))