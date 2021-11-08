
from flask import render_template, redirect, url_for, request
from werkzeug.urls import url_parse

from . import admin_bp

@admin_bp.route('/manager')
def manager():
    return render_template('admin/manager.html')

@admin_bp.route('/professional/<user_name>')
def professional(user_name):
    return render_template('admin/professional.html', user_name=user_name.title())

@admin_bp.route('/formprofesional')
def formprofessional():
    return render_template('admin/formprofessional.html')

@admin_bp.route('/formpatient')
def formpatient():
    return render_template('admin/formpatient.html')