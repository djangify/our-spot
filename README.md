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

## EPICS and User Stories

<details>

Based on the MVT model above, the following EPICS and user stories were created.

## Epics:

***User Authentication and Registration:***
Covering network setup up, user registration, login, and logout functionality.

***User Profiles and Feeds:***
This epic covers user profiles, creating, editing and deleting

***Photo Management:***
How users will add, edit and delete locations.

***Location Detail Page:***
This focuses on the detailed view of a specific location, including comments and likes.

***User Connections:***
The structure for following and displaying the latest activity of followed users.

***Social Interaction:***
Creating a structure for liking, commenting, and sharing locations.

## Admin

***Manage Accounts:***   As an administrator, I want to be able to manage user accounts, including creating, editing, and deactivating them if necessary so that my records are kept up to date.

***Register to add photos:***
 As Admin, I want users to register before being able to book addd a new photo.

***Email notifications:***
As a admin I want to set up a system so users can reset their password if they can not log in.

***Create, Read, Update and Delete***
As admin I want to be able to create, read, update and delete photos and profiles so that the admin area is kept up to date.

## User

***Registration and Log-In***
As a user, I want to be able to register an account, so I can participate in Our Spot and immediately log-in.

***log-In/log out***
As a user, I want to log in and out of my account so that I can access the platform securely.

***Create, Edit, cancel and delete photos:***
As a user I want to be able to create, edit, and delete my photos so that I can stay in control of the information I share.

***View User Photos:***
As a user, I want to be able to view the photos of other users and like them [ANY OTHER ACTIVITY - COMMENT OR SAVE] As a user, I want to view detailed information about a spot when I click on it.

***View User Activity***
As a user, I want to follow other users and see their latest activity on my feed.
As a user, I want to see who is following me and whom I'm following on my profile.

***Create, Edit, cancel and delete profile:***
As a user I want to be able to create, edit, and delete my profile so that I have an accurate record of all my personal information and activity.

***View User Profile:***
As a user, I want to be able to view my profile and latest activity so that I can keep my information up to date.

***View Other Profiles:***
As a user I want to be able to view the profiles of other users so that I can follow their activity.

</details>


**Plain Text Code Block:**

```text
function fibonacci(num, memo) {
  memo = memo || {};

  if (memo[num]) return memo[num];
  if (num <= 1) return 1;

  return memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo);
}
```

