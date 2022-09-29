from datetime import datetime
import calendar

weekdays = ["Monday", "Tuesday", "Wednesday",
           "Thursday", "Friday", "Saturday", "Sunday"]

users = [
    {
    "name": "Michael",
    "bday": datetime(year=2000, month=12, day=27)
    },
    {
    "name": "Traci",
    "bday": datetime(year=1992, month=1, day=26)
    },
    {
    "name": "Bernice",
    "bday": datetime(year=2000, month=3, day=12)
    },
    {
    "name": "Jerry",
    "bday": datetime(year=2017, month=3, day=27)
    },
    {
    "name": "John",
    "bday": datetime(year=2008, month=9, day=16)
    },
    {
    "name": "Monika",
    "bday": datetime(year=1953, month=10, day=24)
    },
    {
    "name": "Nicole",
    "bday": datetime(year=1961, month=5, day=21)
    },
    {
    "name": "Elaine",
    "bday": datetime(year=1970, month=1, day=25)
    },
    {
    "name": "Richard",
    "bday": datetime(year=1959, month=1, day=3)
    },
    {
    "name": "William",
    "bday": datetime(year=1954, month=12, day=3)
    },
    {
    "name": "Carolyn",
    "bday": datetime(year=1966, month=2, day=10)
    },
    {
    "name": "Jason",
    "bday": datetime(year=1964, month=9, day=29)
    },
    {
    "name": "Ayako",
    "bday": datetime(year=1976, month=11, day=28)
    },
    {
    "name": "Rena",
    "bday": datetime(year=1973, month=9, day=10)
    },
    {
    "name": "Zachery",
    "bday": datetime(year=1970, month=7, day=14)
    }
]

def get_birthdays_per_week(users):

        today = datetime.now()
        birthday_list = []
        next_week_db_list = []
        birthdays_week = ""
        user_list = ""
        day_of_week = ""
        next_week_bd_date = ""
        next_week_bd_name = ""
        next_week = []

        for user in users:
            today = datetime.now()
            user_date = user.get('bday').replace(year=today.year)
            print(user_date)

        if user_date.month == datetime.now().month:
            if user_date.day == datetime.now():
                birthday_list.append(user.get('name'))
                user_list = ", ".join(birthday_list)
                print(birthday_name)
                print(current_date)

            if not today.weekday():
                day_of_week = weekdays.get(0)
                print(day_of_week)
            if today.weekday() == user_date.weekday():
                print (f"The list of birthdays is: {birthday_list} {day_of_week}")

            for user in users:
                if user_date.weekday() == weekdays[5] or weekdays[6] and today.weekday() == weekdays[5] or weekdays[6]:
                    next_week = date.today() + timedelta(week + 1)
                    next_week_db_list.append(user.get('name'))
                    next_week_bd_date.append(next_week)
                    next_week_bd_name = ", ".join(next_week_bd_list)
            print(f"The next week list of birthdays is: {next_week_bd_name} {next_week_bd_date}")


        return get_birthdays_per_week

if __name__ == "__main__":
    print((get_birthdays_per_week(users))
