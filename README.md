

Heroku - deploy flask app

1. run in local

be located in the application directory

flask run

http://localhost:5000

2. git

2.1. If change git user

git config --global user.name "abc"

git config --global user.email "abc@gmail.com"

git config  user.name "abc"

git config  user.email "abc@gmail.com"

delete git. credencial 

2.2.

git init

2. Procfile & packages

echo "web: gunicorn app:app" > Procfile

[LIN/WIN]

python3 -m pip install gunicorn==20.0.4

python -m pip install gunicorn==20.0.4

[LIN/WIN]

python3 -m pip freeze > requirements.txt

python -m pip freeze > requirements.txt


3.

Create account in heroku

[CMD/BASH]

heroku login

heroku create a-flask-heroku-app



git add Procfile requirements.txt

git commit -m "Add Heroku deployment files"

heroku create a-flask-heroku-app

-> Creating  a-flask-heroku-app... done

git push heroku master

-->

'''
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (7/7), 3.67 KiB | 1.83 MiB/s, done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Building on the Heroku-20 stack
remote: -----> Determining which buildpack to use for this app
remote: -----> Python app detected
remote: -----> No Python version was specified. Using the buildpack default: python-3.9.7
remote:        To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes
remote: -----> Installing python-3.9.7
remote: -----> Installing pip 20.2.4, setuptools 47.1.1 and wheel 0.36.2
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting click==7.1.2
remote:          Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
remote:        Collecting Flask==1.1.2
remote:          Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
remote:        Collecting gunicorn==20.0.4
remote:          Downloading gunicorn-20.0.4-py2.py3-none-any.whl (77 kB)
remote:        Collecting itsdangerous==1.1.0
remote:          Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
remote:        Collecting Jinja2==2.11.2
remote:          Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
remote:        Collecting MarkupSafe==1.1.1
remote:          Downloading MarkupSafe-1.1.1-cp39-cp39-manylinux2010_x86_64.whl (32 kB)
remote:        Collecting Werkzeug==1.0.1
remote:          Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
remote:        Installing collected packages: click, itsdangerous, MarkupSafe, Jinja2, Werkzeug, Flask, gunicorn
remote:        Successfully installed Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 gunicorn-20.0.4 itsdangerous-1.1.0
remote: -----> Discovering process types
remote:
remote: -----> Compressing...
remote:        Done: 52.7M
remote: -----> Launching...
remote:        Released v3
remote:        https://a-flask-heroku-app.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/a-flask-heroku-app.git
 * [new branch]      master -> master
'''

Verifying deploy in heroku 

[CMD/BASH]

heroku open

4. If errors:

heroku logs --tail

5. buildpack

Login to your Heroku dashboard and open your project.

Go to Settings.

Delete heroku/python from the list of buildpacks

Then click Add buildpack -> Choose "Python" -> Save Changes.

Activate your environment in your code. and run:

heroku ps:scale web=1

-> Scaling dynos... !

https://www.heroku.com/dynos

Dynos are isolated, virtualized Linux containers that are designed to execute code based on a user-specified command. Your app can scale to any specified number of dynos based on its resource demands.

heroku logs --ps web

->

'''
 »   Warning: heroku update available from 7.53.0 to 7.59.0.
2021-09-24T02:46:57.101997+00:00 heroku[web.1]: Starting process with command `gunicorn -b :22920 app:app`
2021-09-24T02:46:58.049526+00:00 app[web.1]: [2021-09-24 02:46:58 +0000] [4] [INFO] Starting gunicorn 20.0.4
2021-09-24T02:46:58.049946+00:00 app[web.1]: [2021-09-24 02:46:58 +0000] [4] [INFO] Listening at: http://0.0.0.0:22920 (4)
2021-09-24T02:46:58.049995+00:00 app[web.1]: [2021-09-24 02:46:58 +0000] [4] [INFO] Using worker: sync
2021-09-24T02:46:58.053062+00:00 app[web.1]: [2021-09-24 02:46:58 +0000] [7] [INFO] Booting worker with pid: 7
2021-09-24T02:46:58.087917+00:00 app[web.1]: [2021-09-24 02:46:58 +0000] [8] [INFO] Booting worker with pid: 8
2021-09-24T02:46:58.380837+00:00 heroku[web.1]: State changed from starting to up
'''

[CMD/BASH]

heroku restart

or

heroku open

Enjoy it!
