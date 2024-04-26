# Meal Planner
Simple back-end for web app, created with Django and Django REST framework.

## Table of Contents
* General info
* Main technologies
* Setup
* Status
* To Do
* Sources

## General info
This web back-end app allows to plan a menu and create an account. Only logged in users have access to their own menu plan and can create, update and delete meals.
By logging in, the user receives a token that should be used by every activity across the app.

## Main technologies
* Django 5.0
* Django REST framework 3.15
  
## Setup
Please make sure you have Python already installed on your machine.
Then, clone this repo to your desktop, activate virtual env and install all dependencies thru pip with a command: `pip install -r requirements.txt`.
Once the dependencies are installed, run `py manage.py runserver` to start the web app on your localhost.

## Status
App is completed and ready to use, however in the future I plan to expand app functionalities (see next paragraph).

## To Do
* Meal plan view by a specific week.

## Sources
"Accounts" part of this app is created based on Ssali Jonathan tutorial "Learn Django REST Framework", published on [youtube](https://www.youtube.com/watch?v=Df7YBcLfPKg&list=PLEt8Tae2spYlosWRH9JDpKNxzb3bSOJGx&ab_channel=SsaliJonathan).
