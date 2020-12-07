# Practical-Project-Repo

The brife: Creating an application that generates objects based upon a set of predefined rules with 4 services.

Service 1 acts as the frontend.

Services 2 and 3 are apis which generate a random object for us.

Service 4 is an api which generates an output based on service 2 and 3.

### Project Tracking

![CIPipeline](https://i.imgur.com/cfy3Tsx.png)

The project was tacked using a kanban board, using githubs build in tracking feature. 

### CI Pipline

![CIPipeline](https://i.imgur.com/wh0ZoFH.png)

The app is built using Python code to create the api, using Flask as a webframework. This lets us use Jinja to template the frontend and display them to the user. The app is hosted using gunicorn 
We are using GitHub as the version control system, so that changes to the source code can be monitored and accesed from a virtual machine or locally.
Jenkins is used to build and deploy the app, building on pushes to git using a git webhook. 
A pipeline is setup in Jenkins to allow for building, testing and deployment to be run automaticaly.

The app is build using docker compose and is deployed using docker swarm. Ansible is used to setup the virtual machines for the swarm, connecting workers to the manager without needing to ssh into each individualy.



### Risk Assesment

|             Problem             |                       Risk                       | Probability | Risk level |                                     Current mitigation                                    |                        Proposed mitigation                        |
|:-------------------------------:|:------------------------------------------------:|:-----------:|:----------:|:-----------------------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| Broken code is deployed to live | Service becomes unavaible                        | Medium      | High       | Test are run before build stage to catch any major errors                                 | Code is checked by second user before being pushed to main branch |
| Swarm Vm goes down              | Service becomes unavaible on that machine        | Low         | Low        | Swarm is setup with multipul workers in case 1 vm goes down                               |                                                                   |
| DDOS attack                     | Service becomes unavaible due to execes trafic   | low         | low        | Nginx is setup to load balance accross each worker to reduce the impact of a DDOS         |                                                                   |
| SSH keys are lost               | Vm can be SSH'd into and code executed           | low         | High       | SSH credentails are kept safe by Jenkins                                                  |                                                                   |
| Swarm attacked on open ports    | Vms can be accessed on open ports on the machine | low         | Medium     | Ngnix is used as a revers proxy to the swarm, so no ports need to be open other than http |                                                                   |

### VCS GitHub

Code was pushed up here to GitHub to be useded in the Jenkins pipeline. The feature branch model was used so that features could be developed indidualy on its own brach, so changes to one feature does not affect another during development.

![Vcs](https://i.imgur.com/dVymnIG.png)


### App design 1st Pass

The inital app was a barebones app with little frontend. Services 2 and 3 were created to make a random number and float respectivly. service 4 returned the product of the 2 numbers in order to test the post request. 

![App1](https://i.imgur.com/EjC8xtL.png)

### Final App design

The final app added in the html frontend, giving a readable output to the user. Services 2 and 3 were created to make a random number and float as before. service 4 returned the product of the 2 numbers in order to test the post request. 

![Appfin](https://i.imgur.com/MAAXrkm.png)



### Pytest

Pytest is ran as used to check if code is working before artifacts are created. It is run as part of the pipeline to prevent images being build if test fail.
Coverage reports created using pytest-cov to check the percentage of the app tested this is done for all 4 services

![pytest](https://i.imgur.com/5WchT7C.png)

![pytest2](https://i.imgur.com/G5B7MWq.png)
![pytest3](https://i.imgur.com/5WchT7C.png)
![pytest4](https://i.imgur.com/5WchT7C.png)

### Future Improvments

I would have added a SQL database to persist data from the app if time permited using a MySQL container.
To keep artifacts more securely and to speed up docker pushes and pulls, I would have add in a private nexus repository to hold images.

