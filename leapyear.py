year = 2024
is_leap_year = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
print(is_leap_year)
