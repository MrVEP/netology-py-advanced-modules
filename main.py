import datetime as dt
import application.salary as salary
import application.db.people as people

if __name__ == '__main__':
    print(dt.datetime.date(dt.datetime.now()))
    salary.calculate_salary()
    people.get_employees()
