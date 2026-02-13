from flask import Flask, render_template, request, redirect, url_for, session, flash
import models 

app = Flask(__name__)
app.secret_key = 'my-secret-key-for-school-project-123'
app.config['SESSION_PERMANENT'] = True


@app.route('/')
def index():
    return render_template('index.html')


# ============== ADMIN ROUTES ==============

@app.route('/admin/verify', methods=['GET', 'POST'])
def admin_verify():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if (username == models.ADMIN_CREDENTIALS['username'] and 
            password == models.ADMIN_CREDENTIALS['password']):
            session['admin_logged_in'] = True
            session['admin_username'] = username
            flash('Login successful! Welcome, Admin.', 'success')

            return redirect(url_for('admin_panel'))
        else:
            flash('Invalid username or password. Please try again.', 'error')
  
    return render_template('admin/admin_verify.html')


@app.route('/admin/panel')
def admin_panel():
    if not session.get('admin_logged_in'):
        flash('Please login first.', 'error')
        return redirect(url_for('admin_verify'))
    all_employees = models.get_all_employees()

    return render_template('admin/admin_panel.html', 
                         employees=all_employees,
                         teams=models.TEAMS)


@app.route('/admin/add_employee', methods=['POST'])
def add_employee():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_verify'))

    employee_id = request.form.get('employee_id')
    name = request.form.get('name')
    team = request.form.get('team')

    if not employee_id or not name or not team:
        flash('All fields are required!', 'error')
        return redirect(url_for('admin_panel'))

    result = models.add_employee(employee_id, name, team)
    
    if result:
        flash(f'Employee {name} added successfully!', 'success')
    else:
        flash(f'Employee ID {employee_id} already exists!', 'error')
    
    return redirect(url_for('admin_panel'))


@app.route('/admin/update_employee', methods=['POST'])
def update_employee():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_verify'))

    employee_id = request.form.get('employee_id')
    name = request.form.get('name')
    team = request.form.get('team')
    result = models.update_employee(employee_id, name=name, team=team)
    
    if result:
        flash(f'Employee {employee_id} updated successfully!', 'success')
    else:
        flash(f'Employee {employee_id} not found!', 'error')
    
    return redirect(url_for('admin_panel'))


@app.route('/admin/delete_employee/<employee_id>')
def delete_employee(employee_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_verify'))
    result = models.delete_employee(employee_id)
    
    if result:
        flash(f'Employee {employee_id} removed successfully!', 'success')
    else:
        flash(f'Employee {employee_id} not found!', 'error')
    
    return redirect(url_for('admin_panel'))


@app.route('/admin/add_bulletin', methods=['POST'])
def add_bulletin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_verify'))
    team = request.form.get('team')
    item = request.form.get('item')
    
    if team and item:
        models.add_bulletin_item(team, item)
        flash(f'Bulletin item added to {team} team!', 'success')
    else:
        flash('Team and item are required!', 'error')
    
    return redirect(url_for('admin_panel'))


@app.route('/admin/logout')
def admin_logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))


# ============== USER ROUTES ==============

@app.route('/user/verify', methods=['GET', 'POST'])
def user_verify():
    if request.method == 'POST':
        employee_id = request.form.get('employee_id')
        employee = models.get_employee_by_id(employee_id)
        
        if employee:
            session['user_logged_in'] = True
            session['employee_id'] = employee_id
            session['employee_name'] = employee['name']
            session['employee_team'] = employee['team']
            
            flash(f'Welcome, {employee["name"]}!', 'success')

            return redirect(url_for('team_dashboard', team=employee['team']))
        else:
            flash('Invalid Employee ID. Please contact admin.', 'error')

    return render_template('user/user_verify.html')


@app.route('/user/team/<team>')
def team_dashboard(team):
    if not session.get('user_logged_in'):
        flash('Please verify your ID first.', 'error')
        return redirect(url_for('user_verify'))

    if session.get('employee_team') != team:
        flash('You do not have access to this team!', 'error')
        return redirect(url_for('team_dashboard', team=session.get('employee_team')))

    bulletin_items = models.get_bulletin(team)
    team_members = models.get_employees_by_team(team)
    template = f'user/{team}_team.html'
    
    return render_template(template,
                         team=team,
                         employee_name=session.get('employee_name'),
                         employee_id=session.get('employee_id'),
                         bulletin_items=bulletin_items,
                         team_members=team_members)


@app.route('/user/logout')
def user_logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)