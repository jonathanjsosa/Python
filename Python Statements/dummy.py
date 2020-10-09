my_list = [('Jonathan', 100), ('Isma', 5000), ('Eli', 800)]


def work_hours_report(my_list):
    max_hours = 0
    employee_of_month = ''

    for employee, hours in my_list:
        if hours > max_hours:
            max_hours = hours
            employee_of_month = employee
        else:
            pass
    return employee_of_month, max_hours


item = work_hours_report(my_list)
print(item)
