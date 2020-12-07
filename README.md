# Practical-Project-Repo

The brife: Creating an application that generates objects based upon a set of predefined rules with 4 services.

Service 1 acts as the frontend.

Services 2 and 3 are apis which generate a random object for us.

Service 4 is an api which generates an output based on service 2 and 3.

### CI Pipline

The app is built using Python code to create the api, using Flask as a webframework. This lets us use Jinja to template the frontend and display them to the user. The app is hosted using gunicorn 
We are using GitHub as the version control system, so that changes to the source code can be monitored and accesed from a virtual machine or locally.
Jenkins is used to build and deploy the app, building on pushes to git using a git webhook. 
A pipeline is setup in Jenkins to allow for building, testing and deployment to be run automaticaly.

The app is build using docker compose and is deployed using docker swarm. Ansible is used to setup the virtual machines for the swarm, connecting workers to the manager without needing to ssh into each individualy.

### App design 1st Pass

The inital app was a barebones app with little frontend. Services 2 and 3 were created to make a random number and float respectivly. service 4 returned the product of the 2 numbers in order to test the post request. 

Image

### Risk Assesment

| Problem                                      | Risk                                                                                                                            | Probability | Risk level | Current mitigation                                                                             | Proposed mitigation                                                |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------|------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| sql db passwords lost(eg uploaded to github) | The database can be accesed by anyone, meaning data could be changed by unauthorised users                                      | Low         | Low        | Use environment variables to store database uri                                                |                                                                    |
| VM goes offline                              | The app will be unusable untill hosted on another Vm                                                                            | low         | Medium     |                                                                                                | Have a backup vm spin up and host the app if the main vm goes down |
| Database goes offline                        | The app won't be able to query the database, rendering the app useless. Updates to the database will be lost, causing data loss | low         | medium     |                                                                                                | Create a backup SQL server                                         |
| Database is attacked/data lost               | Data is lost or deleted using SQL injection, where tables/databases could be dropped using SQL                                  | low         | Low        | Since no sensitive data is being stored, it is not critical to defend against database attacks | Make sure data is regularly backed up to a backup SQL server       |
You can now import Markdown table code directly using File/Paste table data... dialog.

### Pytest


### Future Improvments
