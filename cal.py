# THIS DETERMINES THE DAY OF THE WEEK

def day_of_week(year, month):
  t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
  if month < 3:
    year -= 1
  return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + 1) % 7

# THIS IS THE LEAP YEAR FUNC

def is_leap_year(year):

  try:
    year = int(year)
  except:
    return(print('Hey! Try using some numbers!'))
  
  if (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0):
   return True
  else: 
    return False

# THIS DETERMINES WHAT THE YEAR STARTS ON

def get_days_in_month(month, year):
  months_with_31 = [1,3,5,7,8,10,12]
  months_with_30 = [4,6,9,11]
  months_with_28 = [2]

  if month in months_with_28 and is_leap_year(year) == True:
    return 29
  elif month in months_with_28 and is_leap_year(year) == False:
    return 28
  elif month in months_with_30:
    return 30
  else:
    return 31


# THIS IS THE CALENDAR 

def print_month_cal(month, year):

  the_months = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December'
}

  this_is_the_day_of_week = day_of_week(year, month)
  this_is_the_day_of_the_month = get_days_in_month(month, year)
  month_name = (f"{the_months[month]} {year}")
  cal_header = '   S   M   T   W   T   F   S\n'
  counter = this_is_the_day_of_week
  
  print(f"{month_name:^29}")
  print()
  print(f'{cal_header:>2}')
  print(f"{'    ' * counter}", end='')

  for day in range(1, (this_is_the_day_of_the_month + 1)):
    current_day = f"{day:02}"
    
    if counter < 6:
      print(f"  {current_day:02}", end="")
      counter += 1
    else:
      print(f'  {current_day:02}\n')
      counter = 0
  print()





