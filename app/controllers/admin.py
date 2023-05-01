from app import app, db
from app.forms import CategoryForm
from app.models import Category
from datetime import datetime
from flask import abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required


@app.route('/admin/categories', methods=['POST', 'GET'])
@login_required
def admin_categories_index():
    if current_user.role == 0:
        return abort(403)

    form = CategoryForm()

    if request.method == 'POST' and form.validate_on_submit():
        category = Category.query.filter_by(title=form.title.data).first()

        if category:
            flash('Категория уже существует', 'danger')
        else:
            category = Category(
                title=form.title.data,
                created_at=datetime.now(),
            )

            db.session.add(category)
            db.session.commit()

            flash('Категория создана', 'success')
            return redirect(url_for('admin_categories_index'))

    categories = Category.query.all()

    return render_template('admin/categories_index.html', form=form, categories=categories)
