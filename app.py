from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<ingredient %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        ingredient_content = request.form['content']
        new_ingredient = Drinks(content=ingredient_content)

        try:
            db.session.add(new_ingredient)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your ingredient'

    else:
        ingredients = Drinks.query.order_by(Drinks.date_created).all()
        return render_template('index.html', ingredients=ingredients)


@app.route('/delete/<int:id>')
def delete(id):
    ingredient_to_delete = Drinks.query.get_or_404(id)

    try:
        db.session.delete(ingredient_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that ingredient'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    ingredient = Drinks.query.get_or_404(id)

    if request.method == 'POST':
        ingredient.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your ingredient'

    else:
        return render_template('update.html', ingredient=ingredient)


if __name__ == "__main__":
    app.run(debug=True)
