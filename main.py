from datetime import date, timedelta, datetime

def get_period(start_date: date, days: int):
    result = {}
    for _ in range(days + 1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    return result

def get_birthdays_per_week(users):
    start_date = date.today()
    period = get_period(start_date, 6)
    
    # Створюємо словник для зберігання днів народжень
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    }
    for user in users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month
        if date_bd in list(period):
            user_birthday = user['birthday'].replace(period[date_bd])
            if user_birthday.weekday() in (5,6) and user['name'] not in birthdays_per_week['Monday']:
                if start_date.weekday() != 0:
                    birthdays_per_week['Monday'].append(user['name']) # Переносимо на понеділок
                else:
                    continue
            else:
                day_of_week = user_birthday.strftime("%A")
                if day_of_week not in birthdays_per_week:
                    birthdays_per_week[day_of_week] = [user["name"]]  # Створюємо ключ, якщо його немає
                else:
                    birthdays_per_week[day_of_week].append(user["name"])
    
    result_dict = {}
    for day_name, names in birthdays_per_week.items():
        if names:
            result_dict[day_name] = names

    return result_dict

if __name__ == '__main__':    
    users = [
        {"name": "Bill", "birthday": datetime(1990, 10, 5).date()},
        {"name": "Marry", "birthday": datetime(2000, 9, 3).date()},
        {"name": "Anna", "birthday": datetime(2000, 9, 8).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    
    for day_name, names in result.items():
        if names:
            print(f"{day_name}: {', '.join(names)}")
    
