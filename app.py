from flask import Flask, render_template

app = Flask(__name__)


# Главная страница админки (перенаправляет на профиль или настройки)
@app.route('/')
def index():
    return render_template('profile.html')


@app.route('/profile')
def profile():
    user_data = {"name": "Администратор", "role": "Owner"}
    return render_template('profile.html', user=user_data)


@app.route('/settings')
def settings():
    shop_config = {"name": "Мой Магазин", "currency": "RUB"}
    return render_template('settings.html', config=shop_config)


if __name__ == '__main__':
    app.run(debug=True)
