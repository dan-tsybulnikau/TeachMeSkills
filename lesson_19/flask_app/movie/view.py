from flask import Blueprint, request, redirect, url_for, abort, render_template

movie = Blueprint('movie', __name__,template_folder='templates/movie')

@movie.route('/home', methods=['GET', 'POST'])
def index():
    return {'body': 'no data'}, 999, {"X-Type": 'Data'}

@movie.route('/movie/<int:value>')
def another_index(value):
    print(type(value))
    return "ag"

@movie.errorhandler(410)
def error_gone(error):
    return 'This is not the page you are looking for'