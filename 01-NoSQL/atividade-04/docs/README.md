

Digital Ocean - Large Flask App
https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications


Flask Docs - Modular Apps with Blueprints
http://flask.pocoo.org/docs/1.0/blueprints/


Explore Flask - Configs
http://exploreflask.com/en/latest/configuration.html


Nick Janetakis - 15 Usefull Flask Extensions
https://nickjanetakis.com/blog/15-useful-flask-extensions-and-libraries-that-i-use-in-every-project

Django Docs - MVC vs MVT
https://docs.djangoproject.com/pt-br/2.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names


=========================================
Project structure
=========================================
```code
app
|-- __init__.py
|-- __pycache__
|-- _static
|   |-- 404.html
|   |-- css
|   |   `-- main.css
|   |-- img
|   |   `-- icon.png
|   `-- js
|       `-- main.js
|-- _templates
|   |-- 404.html
|   `-- auth
|       |-- forgot.html
|       |-- signin.html
|       `-- signup.html
`-- auth
    |-- __init__.py
    |-- __pycache__
    |-- controllers.py
    |-- forms.py
    `-- models.py
config/
|-- __pycache__
|-- default.py
|-- development.py
|-- production.py
`-- staging.py
docs/
|-- LICENSE.md
|-- README.md
`-- requirements.txt
tests/
```
