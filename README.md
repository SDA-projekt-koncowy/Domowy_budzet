# Domowy_budzet is a budget calculator app which allows user to keep track of his/her expenses and incomes

## Set up
After cloning repository set up your own virtual environment

```bash
python -m venv path/to/virtual/env
```

Next activate your virtual environment by opening in your venv directory activate.bat file
```bash
your/venv/directory/Scripts/activate.bat
```

Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries

```bash
pip install -r requirements.txt
```

After that migrate app models using

```bash
python manage.py migrate
```
To run the app use the command below and enter the link
```bash
python manage.py runserver
```
![runserver screenshot](images/runserver.PNG) 
## Usage
####After you enter the link you will see the home page for an unauthenticated user
![create account](images/create_account.PNG)
####To create your account click the *Create account* button
####You will see the register form
![register](images/register.PNG)
####Type in your username and password and click submit
####Then you can login with your new account, click on the login button either in the middle of your screen or on the bar at the top
![login](images/login.PNG)
####After you are logged in you will have access to the Income, Expenses and Budget balance tabs.
![logged_in](images/logged_in.PNG)
####You can also see that your username is now presented on the bar at the top, click on it to see more options and then choose the Category panel to add some categories
![options](images/options.PNG)
####Click on the add button and fill out the form with the category you want to use for your incomes and expenses and click submit
![add_category](images/add_category.PNG)
###When you have your categories set up you can start fully using this app
####Add your incomes or expenses under *Income* or *Expenses* tabs, positions that you add will be listed under these tabs and you will be able to update or delete them
![income](images/income.PNG)
![expense](images/expense.PNG)
#### you see your incomes and expenses aggregated under the *Budget balance* tab
![balance](images/kurde_balans_git_majonez.PNG)