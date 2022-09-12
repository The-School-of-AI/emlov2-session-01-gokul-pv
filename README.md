[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8309451&assignment_repo_type=AssignmentRepo)


## What is Docker?
Containers are lightweight, resource-efficient, and portable. They share a single host operating system (OS) with other containers — sometimes hundreds or even thousands of them. By isolating the software code from the operating environment, developers can build applications on one host OS — for example, Linux — and deploy it in Windows without worrying about configuration issues during deployment.


## How to run this repo

This repo provides docker image for influencing an image on any pre-trained timm model. The configuration is done using [Hydra](https://hydra.cc/)

 1. Install docker on your system (refer  [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/))
 2. To build the docker image, first clone the repo and then run 
```docker build --tag (imagename):(tag) . ```
3. Alternatively the image can be pulled from docker hub also using command ```docker pull gokulpv/timmdockerimage:latest ```
4. To run the docker image with default configuration, run the command ```docker run -it gokulpv/timmdockerimage:latest  ```
5. To run the docker image with specific configuration, run the command ```docker run -it gokulpv/timmdockerimage:latest model="timm model name" image="provide image url" ```
