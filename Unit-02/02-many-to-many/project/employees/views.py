from flask import Blueprint, redirect, render_template, request, url_for, flash
#from project.employees.forms import EmployeeForm
from project.employees.models import Employee
from project.employees.forms import EmployeeForm, DeleteForm
from project import db

employees_blueprint = Blueprint(
    'employees',
    __name__,
    template_folder='templates/employees'
)


@employees_blueprint.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    #create new user
    new_employee = Employee(request.form["name"], request.form["years_at_company"])
    #add to the db and then redirect
    db.session.add(new_employee)
    db.session.commit()
    flash("Employee Added!")
    return redirect(url_for("employees.index"))
  return render_template("index.html", employees = Employee.query.all())

@employees_blueprint.route("/new")
def new():
    employee_form=EmployeeForm()
    return render_template("new.html", employee_form=employee_form)

@employees_blueprint.route("/<int:id>/edit")
def edit(id):
    found_employee = Employee.query.get(id)
    employee_form=EmployeeForm(obj=found_employee)
    return render_template("edit.html", employee=found_employee, employee_form = employee_form)

@employees_blueprint.route("/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
  found_employee = Employee.query.get(id)
  if request.method == b"PATCH":
    #edit a user
    found_employee.name = request.form['name']

    db.session.add(found_employee)
    db.session.commit()
    flash("Employee Updated!")
    return redirect(url_for("employees.index"))

  if request.method == b"DELETE":
    #delete a user
    db.session.delete(found_employee)
    db.session.commit()
    flash("Employee Updated!")
    return redirect(url_for("employees.index"))
   return render_template("show.html", employee=found_employee, DeleteForm=DeleteForm)
