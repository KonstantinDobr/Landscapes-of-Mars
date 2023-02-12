from flask import Flask, request, url_for
import os

app = Flask(__name__)


@app.route('/')
def start():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    promotion_list = ['Человечество вырастает из детства.',
                      'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.',
                      'И начнем с Марса!',
                      'Присоединяйся!']
    return '</br>'.join(promotion_list)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <center>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
            alt="здесь должна была быть картинка, но не нашлась">
                        <div>Вот она какая, красная планета.</div>
                    </center>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                    <link rel="stylesheet"
                    href="{url_for('static', filename='css/style.css')}">
                  </head>
                  <body>
                    <center>
                        <h1 id="main_header">Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
            alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-dark" role="alert">
                        Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-info" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                        И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                        Присоединяйся!
                        </div>
                    </center>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                              </head>
                              <body>
                                <center>
                                  <div id='body'>
                                    <h1>Анкета претендента</h1>
                                    <h3>на участие в миссии</h3>
                                    <div>
                                        <form class="login_form" method="post">
                                            <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                            <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                            <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                            <div class="form-group">
                                                <label for="classSelect">Какое у Вас образование?</label>
                                                <select class="form-control" id="educationSelect" name="education">
                                                  <option>Начальное</option>
                                                  <option>Среднее</option>
                                                  <option>Основное</option>
                                                  <option>Профессиональное</option>
                                                </select>
                                            </div>
                                            <div class="form-group">
                                                <label for="form-group">Какие у Вас есть профессии?</label>
                                              <div class="form-check">
                                                  <input type="checkbox" class="form-check-input">
                                                  <label class="form-check-label">Инженер-исследователь</label>
                                              </div>
                                              <div class="form-check">
                                                  <input type="checkbox" class="form-check-input">
                                                  <label class="form-check-label">Инженер-строитель</label>
                                              </div>
                                              <div class="form-check">
                                                  <input type="checkbox" class="form-check-input">
                                                  <label class="form-check-label">Пилот</label>
                                              </div>
                                              <div class="form-check">
                                                  <input type="checkbox" class="form-check-input">
                                                  <label class="form-check-label">Метеоролог</label>
                                              </div>
                                              <div class="form-check">
                                                  <input type="checkbox" class="form-check-input">
                                                  <label class="form-check-label">Инженер по жизнеобеспечению</label>
                                              </div>
                                              <div class="form-check">
                                                  <input type="checkbox" class="form-check-input">
                                                  <label class="form-check-label">Инженер по радиационной защите</label>
                                              </div>
                                              <div class="form-check">
                                                  <input type="checkbox" class="form-check-input">
                                                  <label class="form-check-label">Врач</label>
                                              </div>
                                              <div class="form-check">
                                                  <input type="checkbox" class="form-check-input">
                                                  <label class="form-check-label">Экзобиолог</label>
                                              </div>
                                            </div>

                                            <div class="form-group">
                                                <label for="form-check">Укажите пол</label>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                                  <label class="form-check-label" for="male">
                                                    Мужской
                                                  </label>
                                                </div>
                                                <div class="form-check">
                                                  <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                                  <label class="form-check-label" for="female">
                                                    Женский
                                                  </label>
                                                </div>
                                            </div>

                                            <div class="form-group">
                                                  <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                                  <textarea class="form-control" id="about" rows="5" name="about"></textarea>
                                              </div>

                                            <div class="form-group">
                                              <label for="photo">Приложите фотографию</label></br>
                                              <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>

                                            <div class="form-group form-check">
                                                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                                <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                            </div>
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                        </form>
                                    </div>
                                  </div>
                                </center>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def greeting(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                  </head>
                  <body>
                    <center>
                        <h1>Результаты отбора</h1>
                        <h3>
                        Претендента на участие в миссии {nickname}:
                        </h3>
                        <h3 class="alert alert-success" role="alert">
                        Поздравляем! Ваш рейтинг после {level} этапа отбора
                        </h3>
                        <h3>
                        составляет {rating}!
                        </h3>
                        <h3 class="alert alert-warning" role="alert">
                        Желаем удачи!
                        </h3>
                    </center>
                  </body>
                </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                  <html lang="en">
                    <head>
                      <meta charset="utf-8">
                      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    </head>
                    <body>
                      <center>
                        <h1>Загрузка фотографии</h1>
                        <h2>Для участия в миссии</h2>
                        <div id="photoform">
                          <form method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <label for="photo">Приложите фотографию</label><br/>
                                <input type="file" class="form-control-file" id="photo" name="file">
                            </div><br/>
                            <button type="submit" class="btn btn-primary">Отправить</button>
                          </form>
                        </div>
                      </center>
                    </body>
                  </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        if not os.getcwd().endswith('Загрузка файла\static\img'):
            os.chdir('Загрузка файла\static\img')
        with open('image.jpg', 'wb') as file:
            file.write(f.read())
        return f'''<!doctype html>
                  <html lang="en">
                    <head>
                      <meta charset="utf-8">
                      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    </head>
                    <body>
                      <center>
                        <h1>Загрузка фотографии</h1>
                        <h2>Для участия в миссии</h2>
                        <div id="photoform">
                            <form method="post" enctype="multipart/form-data">
                              <div class="form-group">
                                  <label for="photo">Приложите фотографию</label><br/>
                                  <input type="file" class="form-control-file" id="photo" name="file">
                              </div>
                              <img src="{url_for('static', filename='img/image.jpg')}" 
              alt="здесь должна была быть картинка, но не нашлась"><br/>
                              <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                      </center>
                    </body>
                  </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
                   integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
                   crossorigin="anonymous">
                   </script>
                  </head>
                  <body>
                    <center>
                        <h1>Пейзажи Марса</h1>
                        <div class="carousel slide" data-bs-ride="carousel">
                          <div class="carousel-indicators">
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                          </div>
                          <div class="carousel-inner">
                            <div class="carousel-item active" data-bs-interval="5000">
                              <img src="{url_for('static', filename='img/photo1.jpg')}" class="d-block w-70" alt="здесь должна была быть картинка, но не нашлась">
                            </div>
                            <div class="carousel-item" data-bs-interval="5000">
                              <img src="{url_for('static', filename='img/photo2.jpg')}" class="d-block w-70" alt="здесь должна была быть картинка, но не нашлась">
                            </div>
                            <div class="carousel-item" data-bs-interval="5000">
                              <img src="{url_for('static', filename='img/photo3.jpg')}" class="d-block w-70" alt="здесь должна была быть картинка, но не нашлась">
                            </div>
                          </div>
                        </div>
                    </center>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
