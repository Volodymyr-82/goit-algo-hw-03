from datetime import datetime 

def get_days_from_today(date):
  date_dt=datetime.strptime(date, "%Y-%m-%d").date()
  today=datetime.today().date()
  num_between_days=today-date_dt
  return num_between_days.days

print(get_days_from_today("2021-10-09"))
