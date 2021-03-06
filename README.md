

# Pyramid Learning Journal 
### Code Fellows, Python 401
#### Author: Robert Bronson
#### Deployed URL: https://frightening-blood-49491.herokuapp.com/
### Project Description: 
* The "Pyramid Learning Journal" site is a resource used by the author for posting, editing, and viewing learning journals written while attending Code Fellows' 401 Python course in Seattle, WA. This project is created using the Pyramid web framework for Python.
### Technologies/Resources:
* Python
* Pyramid (web framework)
* HTML/CSS
* Bootstrap (JS, jQuery, etc)
### Routes:
* / - the home page and a list of all LJ posts
* /expense/{id:\d+} - the view to see the detail of a single LJ post
* /expense//journal/new-entry - for adding new LJ posts
* /expense/journal/{id:\d+}/edit-entry - for editing previously created LJ posts
### Set Up and Installation:
* Clone this repository to your local machine.
* Once downloaded, cd into the expense_tracker directory.
* Begin a new virtual environment with Python 3 and activate it.
* cd into the next robert_pyramid_learning_journal directory. It should be at the same level of setup.py
* pip install this package as well as the testing set of extras into your virtual environment.
* $ initialize_db development.ini to initialize the database, populating with random models.
* $ pserve development.ini --reload to serve the application on http://localhost:6543
