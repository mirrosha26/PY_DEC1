from datetime import datetime
from application.salary import calculate_salary
from application.dp.people import get_employees
from termcolor import cprint



if __name__ == '__main__':
    cprint(f'Datetime:   {datetime.now()}', "green", "on_grey")
    calculate_salary()
    get_employees()