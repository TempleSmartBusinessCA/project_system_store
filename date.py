import time
from datetime import date

def get_date():
    today = date.today()
    return today


if __name__ == "__main__":
    today = get_date()
    print(today)

