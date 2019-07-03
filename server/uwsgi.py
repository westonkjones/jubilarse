[uwsgi]
http-socket = 0.0.0.0:6000
module=wsgi
master = true
die-on-term = true
processes = 4
threads = 2
py-autoreload = 1
