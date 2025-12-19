from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Shows the main menu
    return render_template('index.html')

@app.route('/order')
def order():
    # Shows the list of ordered items
    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
