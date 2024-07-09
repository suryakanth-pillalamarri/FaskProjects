from flask import Flask,render_template,request,jsonify,flash,url_for,redirect
from employee import EmployeeForm


app=Flask(__name__)
app.config['SECRET_KEY']='my_secret_key'


@app.route('/')
def index():
    form=EmployeeForm()
    return render_template('index.html',form=form)



@app.route('/submit-employee-details', methods=['POST'])
def employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        try:
            # Process the form data
            employee_name = form.name.data
            employee_age = form.age.data
            employee_department = form.department.data

            # Flash a success message
            flash(f"Employee name {employee_name} added successfully!", "success")
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error processing form data: {e}")
            flash("An error occurred while processing the form data.", "danger")
            return redirect(url_for('index'))
    # Flash validation errors
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in {getattr(form, field).label.text}: {error}", "danger")
    return redirect(url_for('index'))


if __name__=="__main__":
    app.run(debug=True)
