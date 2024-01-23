from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta, MO

# Define the start and end dates
start_date = datetime(2023, 1, 2)  # Monday, January 2, 2023
end_date = datetime(2033, 12, 31)

# Define a list of holidays to exclude
holidays = [datetime(2023, 1, 1),
            datetime(2023, 7, 4),
            datetime(2023, 12, 24),
            datetime(2023, 12, 25),
            datetime(2024, 1, 1),
            datetime(2024, 7, 4),
            datetime(2024, 12, 24),
            datetime(2024, 12, 25),
            datetime(2025, 1, 1),
            datetime(2025, 7, 4),
            datetime(2025, 12, 24),
            datetime(2025, 12, 25),
            datetime(2026, 1, 1),
            datetime(2026, 7, 4),
            datetime(2026, 12, 24),
            datetime(2026, 12, 25),
            datetime(2027, 1, 1),
            datetime(2027, 7, 4),
            datetime(2027, 12, 24),
            datetime(2027, 12, 25),
            datetime(2028, 1, 1),
            datetime(2028, 7, 4),
            datetime(2028, 12, 24),
            datetime(2028, 12, 25),
            datetime(2029, 1, 1),
            datetime(2029, 7, 4),
            datetime(2029, 12, 24),
            datetime(2029, 12, 25),
            datetime(2030, 1, 1),
            datetime(2030, 7, 4),
            datetime(2030, 12, 24),
            datetime(2030, 12, 25),
            datetime(2031, 1, 1),
            datetime(2031, 7, 4),
            datetime(2031, 12, 24),
            datetime(2031, 12, 25),
            datetime(2032, 1, 1),
            datetime(2032, 7, 4),
            datetime(2032, 12, 24),
            datetime(2032, 12, 25),
            datetime(2033, 1, 1),
            datetime(2033, 7, 4),
            datetime(2033, 12, 24),
            datetime(2033, 12, 25)]  # Add more holidays as needed

# Function to check if a date is a weekday and not a holiday
def is_weekday_and_not_holiday(date):
    return date.weekday() < 5 and date not in holidays

# Loop through the dates and print weekdays
current_date = start_date
while current_date <= end_date:
    if is_weekday_and_not_holiday(current_date):
        if (current_date.month == 1 and 15 <= current_date.day <= 21 and current_date.weekday() == 0):
            # Skip MLK Day (Observed Holiday)
            current_date = datetime(current_date.year, current_date.month, current_date.day + 1)
        if (current_date.month == 2 and 15 <= current_date.day <= 21 and current_date.weekday() == 0):
            # Skip President's Day (Observed Holiday)
            current_date = datetime(current_date.year, current_date.month, current_date.day + 1)
        if (current_date.month == 6 and 15 <= current_date.day <= 21 and current_date.weekday() == 0):
            # Skip Juneteenth (Observed Holiday)
            current_date = datetime(current_date.year, current_date.month, current_date.day + 1)
        if (current_date.month == 11 and 22 <= current_date.day <= 28 and current_date.weekday() == 3):
            # Skip Thanksgiving (Observed Holiday)
            current_date = datetime(current_date.year, current_date.month, current_date.day + 1)
        if (current_date.month == 9 and current_date.day <= 7 and current_date.weekday() == 3):
            # Skip Labor Day (Observed Holiday)
            current_date = datetime(current_date.year, current_date.month, current_date.day + 1)
        if (current_date.month == 5 and current_date + timedelta(days=7) > datetime(current_date.year, 6, 1) and current_date.weekday() == 0):
            # Skip Memorial Day (Observed Holiday)
            if (current_date + timedelta(days=1) == datetime(current_date.year, 6, 1)):
                current_date = datetime(current_date.year, 6, 1)
            else:
                current_date = datetime(current_date.year, current_date.month, current_date.day + 1)
        print(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)