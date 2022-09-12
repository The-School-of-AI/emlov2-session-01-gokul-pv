[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8309451&assignment_repo_type=AssignmentRepo)


## What is Docker?
Containers are lightweight, resource-efficient, and portable. They share a single host operating system (OS) with other containers — sometimes hundreds or even thousands of them. By isolating the software code from the operating environment, developers can build applications on one host OS — for example, Linux — and deploy it in Windows without worrying about configuration issues during deployment.

![enter image description here](https://inst-fs-iad-prod.inscloudgate.net/files/2282a013-822c-454c-8add-126e5b7525a5/containers.png?download=1&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2NjI5Njc2OTAsInVzZXJfaWQiOiI3MDAwMDAzMDA2NjY5NSIsInJlc291cmNlIjoiL2ZpbGVzLzIyODJhMDEzLTgyMmMtNDU0Yy04YWRkLTEyNmU1Yjc1MjVhNS9jb250YWluZXJzLnBuZyIsImp0aSI6IjJkZWI4ODYwLTM4NTEtNDA2Ni04ZmViLTYwZjZlNzBiYTg5NSIsImhvc3QiOiJjYW52YXMuaW5zdHJ1Y3R1cmUuY29tIiwib3JpZ2luYWxfdXJsIjoiaHR0cHM6Ly9hNy0xODY4OTA3MDYuY2x1c3RlcjcuY2FudmFzLXVzZXItY29udGVudC5jb20vY291cnNlcy81MTIwMDc4L2ZpbGVzLzE4Njg5MDcwNi9jb3Vyc2UlMjBmaWxlcy8xLWludHJvZHVjdGlvbi10by1tbG9wcy9jb250YWluZXJzLnBuZz9kb3dubG9hZF9mcmQ9MVx1MDAyNm5vX2NhY2hlPXRydWVcdTAwMjZyZWRpcmVjdD10cnVlXHUwMDI2c2ZfdmVyaWZpZXI9ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6VXhNaUo5LmV5SjFjMlZ5WDJsa0lqb2lOekF3TURBd016QXdOalkyT1RVaUxDSnliMjkwWDJGalkyOTFiblJmYVdRaU9pSTNNREF3TURBd01EQXdNREF4TUNJc0ltOWhkWFJvWDJodmMzUWlPaUpqWVc1MllYTXVhVzV6ZEhKMVkzUjFjbVV1WTI5dElpd2ljbVYwZFhKdVgzVnliQ0k2Ym5Wc2JDd2labUZzYkdKaFkydGZkWEpzSWpvaWFIUjBjSE02THk5allXNTJZWE11YVc1emRISjFZM1IxY21VdVkyOXRMMk52ZFhKelpYTXZOVEV5TURBM09DOW1hV3hsY3k4eE9EWTRPVEEzTURZdmNISmxkbWxsZHo5bVlXeHNZbUZqYTE5MGN6MHhOall5T1RjNU16RXdJaXdpWlhod0lqb3hOall5T1RjNU5qRXdmUS5Zc09qeXg1T1JpY1EtaXB0N3gzZTNwYnhCRTRYN0Z1OEJoX3NaVUlnSmlNOFVvdlRmODFCVkpPb0R2YjR1cVg4SnhlbVFFZndiX1B4VWdNbWZ4ckxaUSIsImV4cCI6MTY2MzA1NDA5MH0.N9o6Ey5jIOMHwb0bZp-aQKiTk9sRu_0ZaTD0VBaMzR1KHennWID670uGiQm0f3N3gplwwjcyWrQJKviRswrv-w)

## How to run this repo

This repo provides docker image for influencing an image on any pre-trained timm model. The configuration is done using [Hydra](https://hydra.cc/)

 1. Install docker on your system (refer  [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/))
 2. To build the docker image, first clone the repo and then run 
```docker build --tag (imagename):(tag) . ```
3. Alternatively the image can be pulled from docker hub also using command ```docker pull gokulpv/timmdockerimage:latest ```
4. To run the docker image with default configuration, run the command ```docker run -it gokulpv/timmdockerimage:latest  ```
5. To run the docker image with specific configuration, run the command ```docker run -it gokulpv/timmdockerimage:latest model="timm model name" image="provide image url" ```
