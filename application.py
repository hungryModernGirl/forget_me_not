from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def create_form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
