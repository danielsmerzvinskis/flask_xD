from flask import Flask, render_template, request
from file_proc import read_file

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

@app.route('/params')
def params():
  args = request.args
  for key, value in args.items():
    print(f"{key}:{value}")
  return args

@app.route('/params_table')
def params_table():
  args = request.args
  return render_template('params_table.html', args = args)

@app.route('/chat')
def chat():
  return render_template('chat.html')

@app.route('/test')
def test():
  return render_template('test.html')

@app.route('/test2')
def test2():
  return render_template('test2.html')

@app.route('/post', methods = ["POST"])
def post():
  return request.get_json()

@app.route('/chatok')
def chatok():
  return render_template('chatok.html')

@app.route('/read_file')
def read_from_file():
  content = read_file()
  return content

@app.route('/write_file', methods = ['POST'])
def write_to_file():
  content_type = request.content_type
  if content_type == 'application/json':
    contentJSON = request.get_json()
    write_file(contentJSON['data'])
    return f"Add line {contentJSON['data']} to file."
  else:
    return f"Content type {content_type} is not supported!"
  
@app.route('/file', methods = ['GET', 'POST'])
def workFile():
  if request.method == 'GET':
    return read_from_file()
  elif request.method == 'POST':
    return write_to_file()
  else:
    return f"Method {request.method} is not supported!"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port = 5420, threaded = True, debug = True)