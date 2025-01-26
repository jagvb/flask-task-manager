from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ваш_секретный_ключ'  # Нужен для защиты форм
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # Путь к БД

# Инициализация БД (добавьте после импорта)
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, redirect

@app.route('/add_task', methods=['POST'])
def add_task():
    task_text = request.form.get('task_text')
    # Здесь будет код сохранения в БД
    return redirect('/')
@app.route('/tasks')
def show_tasks():
    tasks = Task.query.all()  # Получаем все задачи из БД
    return render_template('tasks.html', tasks=tasks)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    tasks = db.relationship('Task', backref='user')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))