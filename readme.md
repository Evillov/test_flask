FLASK_APP=app.py flask run


uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app


Конфигурация Nginx для Flask с uwsgi


Последний шаг — настройка проксирования запросов на создаваемый сокет. В Nginx задается имя сайта или IP адрес, порт (обычно 80). Также путь к сокету. Это может быть и TCP сокет.

mcedit /etc/nginx/sites-enabled/todo
server {
listen 80;
server_name todo.example.com;

location / {
include uwsgi_params;
uwsgi_pass unix:/home/todolist/todo.sock;
}

}

Виртуальный хост нужно активировать

ln -s /etc/nginx/sites-availible/todo /etc/nginx/sites-enabled/

Затем проверяем конфигурацию и перезапускаем Nginx

nginx -t
nginx -s reload

Служба должна работать на порту 80

netstat -nltp | grep 80
tcp 0 0 0.0.0.0:80 0.0.0.0:* LISTEN 29624/nginx: master



Устанавливаем нужного владельца на файлы приложения

chown todo -R /home/todolist/

Перезапускаем uwsgi сервис

systemctl restart todo

Настройки на этом завершены. Если возникает 502 ошибка — нужно проверить логи Nginx

tail /var/log/nginx/error.log

Если есть необходимость изменять Unit файл — всегда нужно перезапускать демон Systemd

systemctl daemon-reload