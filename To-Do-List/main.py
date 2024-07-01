from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item_content = request.form['content']
        new_item = TodoItem(content=item_content)
        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    items = TodoItem.query.all()
    return render_template('index.html', items=items)

@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = TodoItem.query.get_or_404(id)
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

if __name__ == '__main__':
    # Create database tables within an application context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
