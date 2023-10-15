import re
import modules.fake_users_generator as fake_users
from datetime import datetime, timedelta
from collections import defaultdict

# Test sample data
# users = [
#     {"name": "Miss Lisa Francis", "birthday": datetime(2008, 6, 27)},
#     {"name": "David Martinez", "birthday": datetime(1977, 10, 21)},
#     {"name": "David Taylor", "birthday": datetime(2003, 10, 19)},
#     {"name": "Jennifer Lewis", "birthday": datetime(1995, 10, 16)},
#     {"name": "Michael Vargas", "birthday": datetime(1987, 10, 23)},
# ]

users = fake_users.main()

today = datetime.today().date()
current_year = datetime.now().year


def weekday_to_number(weekday):
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    return weekdays.index(weekday)


def get_birthdays_per_week(users):
    res = defaultdict(list)
    for d in users:
        birthday = d["birthday"].date()
        # Handle Feb 29 -> use Feb 28
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            birthday_this_year = birthday.replace(year=today.year, day=28)
        delta_days = (birthday_this_year - today).days
        if 0 < delta_days < 7:
            day_of_week = birthday_this_year.strftime("%A")
            if day_of_week == "Saturday" or day_of_week == "Sunday":
                day_of_week = "Monday"
            res[day_of_week].append(d["name"])
    return dict(sorted(res.items(), key=lambda x: weekday_to_number(x[0])))


def pretify_output(userdict):
    res = str()
    for k, v in userdict.items():
        value_string = re.sub(r"\]|\[|'", "", str(v))
        res = res + f"{k}: {value_string}\n"
    res = res.rstrip("\n")    
    return res


if __name__ == "__main__":
    print(pretify_output(get_birthdays_per_week(users)))
