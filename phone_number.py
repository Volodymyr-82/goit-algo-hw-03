import re
def normalize_phone(phone_number):
    need_number=phone_number.strip()
    symbol_del=["-", "(", ")", " ","+"]
    for symbol in symbol_del:
      need_number=need_number.replace(symbol,"")
    if not need_number.startswith('38'):
      need_number="38"+ need_number
    return "+" + need_number

print(normalize_phone("    38050-111-22-22"))
