from flask import Flask
app = Flask("my test proj")

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__ == 'main':
  app.run(debug=True)


  