# Social_Media_Api
This repository contains a REST API built with Python Django and Django REST Framework. It allows users to create an account, log in, and perform CRUD (Create, Read, Update, Delete) operations on posts and comments.

# Installation
Clone this repository to your local machine<br>
#### git clone https://github.com/harshit447/Social_Media_Api.git<br>

Navigate to the project directory.<br>
#### cd Social_Media_Api

Install the required dependencies.<br>
#### pip install -r requirements.txt

Run the server.<br>
#### python manage.py runserver<br>
###### The server will be running at http://127.0.0.1:8000/.

# API Endpoints

Authentication<br>
#### api/auth/register/ - 
Register a new user account<br>
#### api/auth/login/ - 
Obtain a JWT token by passing a valid username and password

# Posts
#### api/posts/ - 
List all posts or create a new post (requires authentication)<br>
#### api/posts/{id}/ - 
Retrieve, update or delete a specific post by ID (requires authentication)<br>
#### api/posts/{id}/like/ - 
Like or unlike a specific post by ID (requires authentication)
# Comments
#### api/posts/{id}/comments/ - 
List all comments for a specific post or create a new comment (requires authentication)
#### api/posts/{id}/comments/{id}/ - 
Retrieve, update or delete a specific comment by ID (requires authentication)
