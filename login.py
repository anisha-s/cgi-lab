#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

import secret
from templates import login_page, secret_page, after_login_incorrect
import os
from http.cookies import SimpleCookie

# set up simple cgi form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

# check if correct login info provided to cgi form
form_ok = username == secret.username and password == secret.password

# set up cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

# checks if cookie data okay
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

# if the data okay then set username to cookie name
if cookie_ok:
    username = cookie_username
    password = cookie_password

# from here everything prints to the html
print("Content-Type: text/html")

if form_ok:
    # set cookie iff login info correct
    print("set-cookie username = ", username)
    print("set-cookie password = ", password)

print()

# load relevent html pages
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())


