ADMIN_CREDENTIALS = {
    'username': 'admin',
    'password': 'admin123'
}

TEAMS = ['creative', 'sound', 'technical']

employees = []

bulletins = {
    'creative': [],
    'sound': [],
    'technical': []
}


def add_employee(employee_id, name, team):
    if get_employee_by_id(employee_id):
        return None
    
    new_employee = {
        'id': employee_id,
        'name': name,
        'team': team
    }
    
    employees.append(new_employee)
    return new_employee


def get_employee_by_id(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            return employee
    return None


def get_all_employees():
    return employees


def get_employees_by_team(team):
    return [emp for emp in employees if emp['team'] == team]


def update_employee(employee_id, name=None, team=None):
    employee = get_employee_by_id(employee_id)
    if employee:
        if name:
            employee['name'] = name
        if team:
            employee['team'] = team
        return employee
    return None


def delete_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        employees.remove(employee)
        return True
    return False


def add_bulletin_item(team, item):
    if team in bulletins:
        bulletins[team].append(item)
        return True
    return False


def get_bulletin(team):
    return bulletins.get(team, [])


def remove_bulletin_item(team, index):
    if team in bulletins and 0 <= index < len(bulletins[team]):
        bulletins[team].pop(index)
        return True
    return False
