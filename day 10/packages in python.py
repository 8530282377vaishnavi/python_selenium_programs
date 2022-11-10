# Packages is a folder which consists of modules and sub packages
# we can access module from package using below syntax
'''import sys
   sys.path.append("path of the package")'''


# import modules from single package




# flask installing in python
# flask is a web framework
# buildding the web application
# also includes HTTP request , Renders template

from flask import Flask
app=Flask(__name__)
@app.route("/")
def Welcome():
    return "Welcome in Flask frame"

app.run()

