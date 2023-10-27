NEED A README AND A TESTING.MD

Project Purpose

Project Objectives and Outcomes

- Model
- Agile Terminologies

EPICS and User Stories

# Our Spot Social Network

A network of people who love to share photos of their favourite spots around the world.

## Project Purpose:

This project has been built to fit into the Code Institute project 4 criteria, the aim of which is to _build a Full-Stack web application that controls a centrally-owned dataset. An authentication mechanism should be used to provide role-based access to the site's data or other activities._

This is the first working draft/prototype of the final project and I will complete this social network once my course has finished. The project includes placeholders in some areas, but all aspects of the project criteria have been covered including implementing a data model, application features and business logic to manage, query and manipulate data

## Project Objectives and Outcomes

<details>
Our Spot is a web application made using Django. It's main aim is to provide a space where people can go to share their favourite places around the world. Places they go to for fun with friends/loved ones or for peace and space away from the world. By sharing individually we collectively build a resource of wonderful spaces to enjoy at a local and global level. As well as sharing the site also provides an opportunity to connect with other members and fosters friendship.

The key objectives of the project include:

- Providing a user-centric experience that encourages sharing and interaction through an intuitive easy to use interface.

- Offering a dedicated space for anyone looking to contribute photos of their favourite spot including local parks, open spaces and hangouts, with an opportunity to share what there is to do and why they love it.

- An opportunity for people to engage and interact with each other through comments, fostering connecting and opening dialogue. Profiles are provided for each member that can be followed by other members.

- Building a database-backed MVC web application that lets users store and manipulate data records including the ability to create, edit and delete.

- Giving users the ability to initiate and control their actions while providing immediate and complete feedback on data processes.

- A place where administrators of the project have a panel that allows them to monitor users and the information they share as well as the comments they make, to ensure the community is kept safe and the environment is not abused.

The end result has been a user-friendly photo sharing network that has been encouraged and informed through user research and engagement.

</details>

## Model Views Template (MVC) for scheduler

<details>
I used MVT to help define the project's requirements, features, and structure by considering the following questions

**Model :**

- What data do we need to store in the database for this network? E.g. username, password, photo etc
- What are the attributes of a User profile for the members?
- What information should be associated with a location (or spot) shared by users.
- What profile is needed to represent users and their attributes?

**View :**

- What should users see when they first visit the website (homepage)?
- How do we display the latest locations shared by all users and by the user alone.
- What views or pages are needed for users to register and log in?
- How should the process to add new locations be structured in terms of user interactions and views?
- What information should be displayed on a users profile page?

**Template :**

- What should the HTML structure of the site look like? What is the layout for the pages?
- What should the structure and design of the user registration and login forms look like?
- What does the users template to add, edit and delete locations look like? How should they be structured?
- What should these templates include?
- What should the format and style of a users profile page look like?

**Authorization :**

- How will users authentication and authorization be handled to ensure that only authorised users can add photos?
- Do we need to integrate any third-party services for features like email notifications?
- How will errors and validation on user input be handled?
- What testing strategies will be employed to ensure the system functions correctly?
- How will user acceptance testing (UAT) be handled?

These questions lay the groundwork for creating user stories, developing the database schema, designing templates, and implementing the necessary views and functionality within Django.

</details>

## Agile Terminologies

<details>

- Create backlog

- Divide work into sprints

- Create subset sprints

- Review work - completed yesterday, to do today, any challenges

- Testing - developer tool, (print) command, keep an eye on terminal/console area.

- Obtain feedback.

- Maintain product backlog and prioritise items/adapt to change
Future implementations/scalability and performance optimisation.
</details>

## Target Audience

The Our Spot social network has been designed for:

Nature lovers who enjoy being outside and who appreciate the health benefits of spending time in nature.

People looking to share the places they love to visit as well as people looking for places to visit, whether that is for something to do on a romantic date or a place to go to enjoy solitude.

Photographers and travellers who love to share some of their favourite spots around the world.

## Research

<details>
This project came about as a result of an online workshop with adult education participants. Talk turned to weekend activities and a discussion was had about finding a network where the emphasis wasn't on highlighting what people had but instead focused on where people went (activities and experiences) and what they liked to do - simple, mainly free things that can be enjoyed alone or with family/friends/loved ones.

After hearing a Willow Smith song called Our Spot I undertook a focus group to find out what people would enjoy doing on a social network that offered an opportunity to simply share their favourite places to go and meet up.

As a result of the focus group the emphasis was on keeping the site simple (e.g. photos only) and encouraging people to share where they go, what they enjoy doing and why its their favourite spot. I arranged a couple of small focus groups before planning on the design of the site (which changed a few times) and starting the project.

</details>

## User Features / Design

<details>
As a result of the focus groups it was agreed that as a member of the network users will enjoy:

- A network that focuses on the importance of spending time outside

- The opportunity for users to share their experiences and activities through photographs

- An opportunity to interact with other members through comments and the follow system

- A user-friendly dashboard that provides access to all parts of the network easily

- A user-friendly system/user journey for adding, commenting on and liking photos

- A user-friendly design that works across all devices

- Simplicity in registering, using and interacting were the main priorities

This research fed into the MVC and user stories.

</details>

## EPICS and User Stories

Based on the MVT model above, the following EPICS and user stories were created to support project development.

[View my GitHub Project Board Here](https://github.com/users/todiane/projects/8/views/1?layout=board)

## EPICS:

<details>
A total of six EPICS were created and organised into sprints.

**_User Authentication and Registration:_**
Covering network setup up, user registration, login, and logout functionality.

**_User Profiles and Feeds:_**
This epic covers user profiles, creating, editing and deleting

**_Photo Management:_**
How users will add, edit and delete locations.

**_Location Detail Page:_**
This focuses on the detailed view of a specific location, including comments and likes.

**_User Connections:_**
The structure for following and displaying the latest activity of followed users.

**_Social Interaction:_**
Creating a structure for liking, commenting, and sharing locations.

## Admin

**_Manage Accounts:_** As an administrator, I want to be able to manage user accounts, including creating, editing, and deactivating them if necessary so that my records are kept up to date.

**_Register to add photos:_**
As Admin, I want users to register before being able to book addd a new photo.

**_Email notifications:_**
As a admin I want to set up a system so users can reset their password if they can not log in.

**_Create, Read, Update and Delete_**
As admin I want to be able to create, read, update and delete photos and profiles so that the admin area is kept up to date.

## User

**_Registration and Log-In_**
As a user, I want to be able to register an account, so I can participate in Our Spot and immediately log-in.

**_log-In/log out_**
As a user, I want to log in and out of my account so that I can access the platform securely.

**_Create, Edit, cancel and delete photos:_**
As a user I want to be able to create, edit, and delete my photos so that I can stay in control of the information I share.

**_View User Photos:_**
As a user, I want to be able to view the photos of other users and like them [ANY OTHER ACTIVITY - COMMENT OR SAVE] As a user, I want to view detailed information about a spot when I click on it.

**_View User Activity_**
As a user, I want to follow other users and see their latest activity on my feed.
As a user, I want to see who is following me and whom I'm following on my profile.

**_Create, Edit, cancel and delete profile:_**
As a user I want to be able to create, edit, and delete my profile so that I have an accurate record of all my personal information and activity.

**_View User Profile:_**
As a user, I want to be able to view my profile and latest activity so that I can keep my information up to date.

**_View Other Profiles:_**
As a user I want to be able to view the profiles of other users so that I can follow their activity.

</details>

# Site Structure

When designing the structure of the site I kept my focus on the need to create a web-based application that has both a user interface (front end) and server-side logic database (back end) stored in a central location. The most important feature was the ability for users to interact with this interface and manipulate the data through CRUD capabilities, while providing clear updates on any changes made.

Wireframes HERE

## Database structure

<details>

Postresql was used to create the data structure. There were a few challenges with the database which meant I had to reset it and start again. This mainly happened if I changed and then went to migrate a models.py file.

I contacted Tutor support for help recusing my database the second time but unfortunately it wasn't possible. They managed to re-create my site over at GitPod so it was mainly a Codeanywhere issue. I had to delete my workspace and create a new one, which also meant I had to reinstall everything in my requirements.txt file.

The first time it happened I had added several user profiles to give me insights into how the images were behaving once uploaded. After the second database crash I decided to only include two users with three photos each until the site was complete. I then added additional users.

Image of database

</details>

## CRUD functionality

<details>

The ability to create, read, update and delete data has been created using the following:

**_Users:_**

- A dashboard where members can read about their latest uploads as well as gain access to view, edit and delete them.

- A page dedicated to creating new uploads with a simple interface.

- Pages where users can edit and delete any information they have uploaded.

- The ability to follow users and like the photos of other members.

- The ability to create and delete comments.

**_Admin:_**

A central location where the site can be managed including the ability to create, read, edit and delete:

- members
- locations/photos added by members
- profiles
- comments

</details>

## Authentication and Authorisation

<details>

Authorisation is only available to registered users so the site is hidden away and register details available on the homepage with a login link in the navigation bar. If a non-member clicks the log-in link they are invited to register.

Email requirement is not necessary to become a member. Only user name and password are essential items, making registration quick and easy.

Once registered a new users is invited to log-in and will be taken straight to the dashboard where they can update their profile and/or add a new location photo.

Image OF HOMEPAGE

IMAGE OF REGISTRATION PAGE

IMAGE OF LOGIN PAGE FOR NEW USERS

IMAGE OF LOGIN PAGE

IMAGE OF DASHBOARD

## Password Management

INFORMATION ON RESETTING PASSWORD
can be done inside the site (photo)

</details>

## Navigation

A simple navigation was created using Bootstrap Navbar. Only logged-in users can see the pages available. Unregistered and logged out users only see the ability to log in.

PHOTO

## Dashboard

After logging in users are taken to their dashboard where they are presented with a list of their recent uploads.
They also have the ability to view and edit their profile

PHOTO OF DASHBOARD

## Recently added

This page contains the photos of all members and infinite scroll has been used so that members can scroll down and look through the photos.

PHOTO OF PAGE

When a user clicks on a photo they are taken to a display page. If they are the owner of the photo they have the ability to edit and delete the photo. If they are not users can comment and like the photo.

## Add New Spot

This area has been kept fairly simple. Users can add a title, description (up to 500 words), photo and to ensure the alt feature is added users are encouraged to describe their photo.

PHOTO OF ADD NEW SPOT

## Edit, Delete Spot

The ability to edit or delete any photo uploaded by a user is available on their dashboard and also shows up on locations they have added.

PHOTO OF LOCATION_DETAIL.HTML PAGE

## Likes and Comments

The ability to like and comment on a photo is available to all users. The ability to delete a comment has also been included

PHOTO OF LIKE AND COMMENT AND DELETE

## Report profile and/or photo

There is a link available for members who want to report a profile or photo. A pop up box appears and once submit is pressed a message confirming that Admin will take a look is shown.

PHOTO OF REPORT LINK

PHOTO OF MESSAGE

## List of Members

This page contains a list of profile photos with the name of the user. This can be clicked and a full profile appears.

LIST OF MEMBERS

## User Profile

Each member is provided with a profile however adding a photo is optional.

PHOTO OF PROFILE

## Follow A Member

There is a follow button on the profile of each member so users can follow each other.

PHOTO OF FOLLOW BUTTON

## Placeholders and Future Updates

The network includes a few placeholders that were adding so show additional features that will be included. These are:

_Report a photo or profile_ - The button under photos and profiles can be clicked to report a photo/profile to Admin. This currently works on the network but is not connected to an email system right now.

_Email password_ - If a member is unable to log-in because they have forgotten their password the ability to complete the "forgotten password" form is available but is not currently a working system.

As a social network there were a number of features that will be added at a later date. Future features include:

- Email authentication - the ability to sign up using email and receive notifications via email.

- The ability to search for images based on tags

- Album creation so photos can be saved into specific albums, e.g. parks, holiday etc

- Personalised recommendations - users receive recommendations for new spots based on previous uploads

- A feed that shows user activity and trending images

## Testing

Please see separate Testing MD HERE include INFORMATION ON BUGS on this page.

## Deployment

Deployment took place immediately after installing Django and Heroku was set to manual deployment for much of the project.

## Technologies Used

**_Core Resources:_**

- Django
- Python
- HTML
- CSS
- Bootstrap
- JavaScript & JQuery
- Postgresql
- GitHub
- GitHub projects

**_Project Resources_**

- ElephantSQL
- Heroku
- Cloudinary
- CodeAnywhere
- Visual Studio Code
- Google Developer Tools

**_Additional Resources_**

- Beautifier.io - to reform JavaScript - https://beautifier.io/
- Images - my own plus Pexel
- Favicon
- DrawSQL -
- Changing images to webp
- Balsamiq for wireframes

## Resources Used

- Django 4 by Example book

- Daisy (link to video)

- Tomi (link to video)

- Infinite Scroll (link)

## Acknowledgements

- Research and focus group participants
- Daisy

- Slack community and Tutor support
