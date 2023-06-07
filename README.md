# CICD Interview Test
## Interviewer Project 

In this project you will work on 3 main topics:
- Kubernetes
- Python
- Jenkins pipelines

You will get 90 minutes to complete the project.
Each topic is estimated to take 30 minutes.

## Kubernetes

You are going to deploy a simple app that runs on a kubernetes cluster.
The app is a simple Flask webapp that connects to a mongoDB instance.
The webapp requires only 100Mi of ram to run properly.

In the CICD\Kubernetes\Yamls you have most of the needed yamls for the app deployment.

What you need to do:

- Fill in the pvc.yaml file so the mongodb will be able to write its data.
- The pvc should use a storage class named ceph-rbd-sc, the pvc size should be 5Gi.
- Change the mongo statefulset so the root username and password will be admin admin.
- Write a nodePort service for the webApp (port: 5000, targetPort: 5000, nodePort: 32500)
- If you find anything else you need to change in the yamls in order to run the application. do it!


The cluster might have its own errors and bugs, handle them and fix anything that comes up!

In order to login into the cluster run:.

```sh
ssh -i devops@<IP>
(password: interviewPassword)
```

In order to validate that your app is actually working, you will have to nevigate to 3 different API's.
The webapp itself will guide you what to do in oreder to test the app (The instruction are in the main page http://<WorkerIp>:32500) 


## Python

This section will test your python skills.
The section does not related to the kubernetes one.
You can find a file named Tweets.json under the folder CICD/Python.
This file is a simple Json file that contains different tweets from several usernames from different times.
Write a new python script that will have the next 2 function:

- mostLikableTweet - A function that finds what tweet is the most likable one. The function will print the content of the tweet, the username and the likes number.
- mostLikesPerUser - A function that finds what username has the most likes. The function will print the username and the total likes he got.



## Jenkins Pipelines

The last step of this project is going to deal with a CI / CD while focusing on the CI part.

In the kubernetes cluster under the devops-tools namespace there is a jenkins pod.
find its service and login into the Jenkins UI with the credetails below:
```sh
username: admin
password: admin
```

Now, the subtasks we want you to complete are:

1. Write a Dockerfile that will create a docker image which runs the python script you wrote earlier. The Image should also have the flask module installed.
2. Create a Jenkinsfile that builds this docker image, tags it and pushes it into dockerhub using the credentials you were given before. The tag should look like python-script:<BUILD_NYMBER>.
3. Use this Jenkinsfile so run the job "my-job" on the Jenkins UI. The trigger can be by clicking the build now button.



### Good Luck !!

