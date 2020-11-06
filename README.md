## E-COMMERCE


## AUTHOR
    * By AokoMercyline

## DESCRIPTION
* This is a minimal REST API Django project for an online trading store.
:satisfied:


## BEHAVIOUR DRIVEN DEVELOPMENT



## Project live site
  This is the live .[ Click for the demo]()
 

## FEATURES
* To access endpoint for register
- run this link https://ecommercendpoint.herokuapp.com/api/register/
* To access endpoint for login
- run this link https://ecommercendpoint.herokuapp.com/api/login/
* To access endpoint for profile
- run this link https://ecommercendpoint.herokuapp.com/api/users/0/profile/
* To access endpoint for change-password
- run this link https://ecommercendpoint.herokuapp.com/api/change-password/



## SETUP INSTALLATION

1.Clone or download and unzip the repository from github,https://github.com/AokoMercyline/E-commerce

2.Activate virtual environment using python3.8 as default handler virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate

3.Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

4.Create the Database

* psql
* CREATE DATABASE instacopy;
5.Create .env file and paste paste the following filling where appropriate:

- SECRET_KEY = '<Secret_key>' 
- DBNAME = 'ecommerce'
- USER = ''
- PASSWORD = '' 
- DEBUG = True

6.  Run initial Migration 
    - python3 manage.py makemigrations instagram 
    - python3 manage.py migrate .Run the app 
    - python3 manage.py runserver 
    
## TECHNOLOGIES USED
* Python 3.8
* Django-Rest-Framework
* knox
* django_rest_passwordreset
* Postgress
* corsheaders

## SUPPORT and Contact

contact me aokomercyline34@gmail.com

## LICENSE
The project is under[MIT license](/blob/master/LICENSE)
Copyright &copy; 2020.All rigths reserved
  