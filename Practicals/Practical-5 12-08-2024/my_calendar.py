import calendar

# Set the first day of the week to Sunday
calendar.setfirstweekday(calendar.SUNDAY)

# Year 56 AD
year = 56

# Print the calendar for the entire year, starting from Sunday
print(calendar.TextCalendar().formatyear(year))
