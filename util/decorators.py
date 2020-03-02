from flask import render_template, redirect, url_for
from flask_login import current_user


def admin_route(func):
    def check_admin(*args, **kwargs):
        print(hasattr(current_user, 'category'))
        if hasattr(current_user, 'category') and current_user.category != 'admin':
            return render_template('notfound.html')
        return func(*args, **kwargs)
    check_admin.__name__ = func.__name__
    return check_admin


def is_not_logged_in(func):
    def check_logged_in_user(*args, **kwargs):
        if hasattr(current_user, 'name') and current_user.name:
            return redirect(url_for('index.home'))
        return func(*args, **kwargs)
    check_logged_in_user.__name__ = func.__name__
    return check_logged_in_user
