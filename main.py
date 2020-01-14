from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hi!</h1>"
  
@app.route('/home')
def home():
  return render_template('home.html', aktiva_lapa ="home")

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contacts')
def contacts():
  return render_template('contacts.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port = 5420, threaded = True, debug = True)

