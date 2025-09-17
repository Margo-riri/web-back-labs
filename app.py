from flask import Flask, url_for, request, redirect
from datetime import datetime  

app = Flask(__name__)

count = 0

@app.route("/")
@app.route("/web")
def start():
    return """<!doctype html>
        <html>
            <body>
                <h1>web-сервер на flask</h1>
                <a href="/author">Информация об авторе</a>
            </body> 
        </html>""" 

@app.route("/author")
def author():
    name = "Размахнина Маргарита Михайловна"
    group = "ФБИ-31"
    faculty = "ФБ"
    return f"""<!doctype html>
        <html>
            <body>
                <p>Студент: {name}</p>
                <p>Группа: {group}</p>
                <p>Факультет: {faculty}</p>
                <a href="/web">web</a>
            </body>
        </html>"""

@app.route('/image')
def image():
    path = url_for("static", filename="ka.jpg")
    return '''
<!doctype html>
<html>
    <body>
        <h1>Тимон</h1>
        <img src="''' + path + '''">
    </body>
</html>'''

@app.route('/counter')
def counter():
    global count
    count+=1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr

    return '''
<!doctype html>
<html>
    <body>
        Сколько раз сюда заходили: '''+ str(count) + '''
        <hr>
        Дата и время: ''' + time + '''<br>
        Запрошенный адрес: ''' + url + '''<br>
        Ваш IP-адрес: ''' + client_ip + '''<br>
    </body>
</html>'''

@app.route('/info')
def info():
    return redirect('/author')

@app.route('/lab1/created')
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''', 201

