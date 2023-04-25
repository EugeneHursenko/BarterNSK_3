from app import app
from app.forms import CategoryForm
from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user


@app.route('/admin/categories', methods=['POST', 'GET'])
@login_required
def admin_categories_index():
    if current_user.role == 0:
        return abort(403)

    form = CategoryForm()

    if request.method == 'POST':
        # @todo создание категрии

        flash('Категория создана', 'success')
        return redirect(url_for('admin_categories_index'))

    return render_template('admin/categories_index.html', form=form)
