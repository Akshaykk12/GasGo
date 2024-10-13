# GasGo
## Introduction

Django application to provide consumer services for gas utilities. The application would allow customers to submit service requests online, track the status of their requests and view their account information.
The application would also provide customer support representatives with a tool to manage requests and provide support to customers.

## Screenshots
![Default Home View](homepage.png?raw=true "Title")
![Default Home View](orders_and_tracking.png?raw=true "Title")

### Main features

* Service requests: The application would allow customers to submit service requests online. They have the ability to select the type of service request.

* Request tracking: The application would allow customers to track the status of their service requests. This would include the ability to see the status of the request, the date and time

* Add Products: Adninistration can add or remove products/ services for the customers as per the availibility.

* Administration Management: Administration can manage the products, orders, customers.



## Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/Akshaykk12/GasGo.git
    $ cd ./gasgo
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
