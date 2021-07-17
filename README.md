YTubers – A Django based web application for youtubers
===

  A web portal where companies can hire youtubers based on the youtuber’s experience and interests for promoting their events in youtube. 	
This project was developed using Django with PostgreSQL as the database for storing the details regarding the users of the portal as well as the youtubers registered.

## Directions to use : 
1. Download the git hub folder or clone it to your local machine.
2. The packages required to run the project are mentioned inside the requirements.txt. 
3. Create a virtual environment by `pipenv shell`.
4. Open up the code editor and execute `pip install -r requirements.txt` for installing all the required packages.
5. Go to the tubers folder where manage.py is present and run the command `python manage.py runserver`.

## Main features : 
### Home Page : 
  Features for user authentication using Django (sign in, sign out), keyword search, display of featured youtubers as well as other youtubers along with the team.

<img src="https://raw.githubusercontent.com/anulrajeev/Ytubers_github_images/master/home.png" height=500px >

Bottom of the page :
<img src="https://raw.githubusercontent.com/anulrajeev/Ytubers_github_images/master/home2.png" height=500px >

### Registration page for new users :
<img src="https://raw.githubusercontent.com/anulrajeev/Ytubers_github_images/master/register.png" height=500px>

### Login feature for alredy registered users :
<img src="https://raw.githubusercontent.com/anulrajeev/Ytubers_github_images/master/login.png" height=500px>

### Dashboard for logged in users showing the youtubers whom they have hired in the past :
<img src="https://raw.githubusercontent.com/anulrajeev/Ytubers_github_images/master/dashboard.png" height=500px>

### Facility for youtubers to join the platform to get hired :
<img src="https://github.com/anulrajeev/Ytubers_github_images/blob/master/join_platform.png" height=500px>

### Individual pages for each youtuber along with a facility to hire them
<img src ="https://github.com/anulrajeev/Ytubers_github_images/blob/master/youtubers_details.png" height=500px>
<img src ="https://github.com/anulrajeev/Ytubers_github_images/blob/master/youtubers_details2.png" height=500px>
