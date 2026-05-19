from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html,about.html,contact.html,work.html,project.html, style.css')

if __name__ == '__main__':
    app.run(debug=True)