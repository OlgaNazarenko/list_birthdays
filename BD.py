from datetime import datetime, timedelta


USERS = [
    {
        "name": "Michael",
        "bday": datetime(year=2000, month=10, day=2)
    },
    {
        "name": "Traci",
        "bday": datetime(year=1992, month=9, day=30)
    },
    {
        "name": "Bernice",
        "bday": datetime(year=2000, month=3, day=12)
    },
    {
        "name": "Jerry",
        "bday": datetime(year=2017, month=10, day=7)
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

def get_birthdays_per_week(users: list[dict]):

    today = datetime.today()

    start_current_week = (today - timedelta(2 + today.weekday()))
    end_current_week = (today + timedelta(4 - today.weekday()))
    end_next_week = (today + timedelta(4 - today.weekday() + 7))

    birthdays_current_week: dict[list] = {}
    birthdays_next_week: dict[list] = {}

    for user in users:
        birthday: datetime = user['bday'].replace(year=today.year)

        if start_current_week <= birthday <= end_next_week:
            name_weekday = "Monday" if birthday.weekday() in (5, 6) else birthday.strftime("%A")

            if birthday <= end_current_week:
                if birthdays_current_week.get(name_weekday):
                    birthdays_current_week[name_weekday].append(user['name'])
                else:
                    birthdays_current_week[name_weekday] = [user['name']]

            else:
                if birthdays_next_week.get(name_weekday):
                    birthdays_next_week[name_weekday].append(user['name'])
                else:
                    birthdays_next_week[name_weekday] = [user['name']]


    print(f"The list of birthdays next week is: {birthdays_next_week}")
    print(f"The list of birthdays this week is: {birthdays_current_week}")

if __name__ == "__main__":
    get_birthdays_per_week(USERS)
