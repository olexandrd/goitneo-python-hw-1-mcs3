import re
import ast
import json
from faker import Faker
from datetime import datetime

FAKE_USERS = 1000

fake = Faker()


def generate_users_list(users_count):
    res = list()
    for i in range(users_count):
        new_user = {"name": fake.name(), "birthday": fake.date_time()}
        res.append(new_user)
    return res


def main():
    return generate_users_list(FAKE_USERS)


if __name__ == "__main__":
    main()
