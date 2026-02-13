function editEmployee(id, name, team) {
            // Show the update section
            document.getElementById('update-section').style.display = 'block';
            
            // Fill the form with current employee data
            document.getElementById('update_employee_id').value = id;
            document.getElementById('update_name').value = name;
            document.getElementById('update_team').value = team;
            
            // Scroll to the update form
            document.getElementById('update-section').scrollIntoView({ behavior: 'smooth' });
        }

        function cancelEdit() {
            // Hide the update section
            document.getElementById('update-section').style.display = 'none';
            
            // Clear the form
            document.getElementById('update-form').reset();
        }