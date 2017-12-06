from flask import Blueprint, redirect, render_template, request, url_for, flash
#from project.employees.forms import EmployeeForm
from project.departments.models import Department
#from project.departments.forms import DepartmentForm
from project import db

# let's create the owners_blueprint to register in our __init__.py
departments_blueprint = Blueprint(
    'departments',
    __name__,
    template_folder='templates'
)
@departments_blueprint.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    #create new user
    new_department = Department(request.form["name"])
    #add to the db and then redirect
    db.session.add(new_department)
    db.session.commit()
    flash("Department Added!")
    return redirect(url_for("departments.index"))
  return render_template("index.html", departments = Department.query.all())


@departments_blueprint.route("/new")
def new():
    department_form=DepartmentForm()
    return render_template("new.html", deparment_form=department_form)

@departments_blueprint.route("/<int:id>/edit")
def edit(id):
    found_department = Department.query.get(id)
    department_form=DepartmentForm(obj=found_department)
    return render_template("edit.html", department=found_department, department_form = department_form)

@departments_blueprint.route("/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
  found_department = Department.query.get(id)
  if request.method == b"PATCH":
    #edit a user
    found_department.name = request.form['name']

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
