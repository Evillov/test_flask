from flask import Flask
from flask import render_template

app = Flask("name")


@app.route('/hello/<name>&<name2>')
def hello(name,name2):
  return render_template('hello.html', name=name, name2=name2)

if __name__ == 'main':
  app.run(debug=True) 
  #FIXME: to be updated.
  #TODO:
  # debug true задаем специально для разработки (в данном случае при обновление/изменение
  # кода приложение автоматически само обновит данные на сайте)