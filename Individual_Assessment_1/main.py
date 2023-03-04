from flask import Flask, render_template
from datetime import date

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def report():
    return render_template("report-"+str(date.today())+".html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)