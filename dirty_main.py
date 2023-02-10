from datetime import date
import PySimpleGUI as sg

from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    today = date.today()
    salary = calculate_salary('Анна')
    employees = get_employees()
    layout = [[sg.Text(f'Запущен dirty_main {today}')],
              [sg.Text(f'calculate_salary: {salary}')],
              [sg.Text(f'get_employees: {employees}')],
              [sg.Button('OK')]]
    window = sg.Window('main.py', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
            break

