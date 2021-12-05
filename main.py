from application import salary, people
from datetime import datetime as dt


if __name__ == '__main__':
    salary.calculate_salary()
    now_time = dt.now()
    print(now_time)
    people.get_employees()
    utc_now = dt.utcnow()
    print(utc_now)
    delta = now_time - utc_now
    print(delta)
