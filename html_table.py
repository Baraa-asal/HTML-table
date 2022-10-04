from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    users = (
        {'first_name': 'Baraa', 'last_name': 'AboAsal'},
        {'first_name': 'Afnan', 'last_name': 'AboAsal'},
        {'first_name': 'Bayan', 'last_name': 'AboAsal'},
        {'first_name': 'Yaseen', 'last_name': 'AboAsal'}
    )
    return render_template('index.html', user=users)


if __name__ == "__main__":
    app.run(debug=True)
