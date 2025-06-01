from datetime import datetime 

def get_days_from_today(date):
  try:
    date_dt=datetime.strptime(date, "%Y-%m-%d").date()
  
    today=datetime.today().date()
    num_between_days=today-date_dt
    return num_between_days.days
  except ValueError:
    print(f'{date} — невірний формат дати (потрібно вводити YYYY-MM-DD)')
print(get_days_from_today("2021-11-09"))
