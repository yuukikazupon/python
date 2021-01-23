#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
print("Content-Type:text/html;charset=utf-8")
print("")

print("<pre>")
form = cgi.FieldStorage()
# print(form)

mode = form.getvalue("mode",default="")
print("mode=",mode)

print("-----all params-----")
# print(form.keys())
for k in form.keys():
    print(k,"=",form.getvalue(k))
