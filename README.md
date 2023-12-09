# Challenge-Accepted

## Start Challenge-Accepted:

Getting started:

1. Install:

   - VSCode
   - WSL2
   - DockerDesktop

2. In Terminal in Challenge-Accepted root directory
   - docker-compose build
   - docker-compose up

Backend (Swagger) now runs on:
http://localhost:8000/docs

Frontend now runs on:
http://localhost:3000/

Database Connection if needed:
http://localhost:5050/
email: challenge-accepted@gmail.com
pw: password

Strg + C/docker-compose down to stop

For more help with the docker commands, have a look at our HELP.md

## Deployed Release

There is also a deployed version of the Challenge-Accepted.
You can find it under: http://3.78.244.229:3000/#/login

## Start Challenge-Accepted without docker-compose (optional):

cd backend
uvicorn src.main:app
http://127.0.0.1:8000/docs

frontend:
cd frontend
npm install
npm run dev

### install dev software backend:

Install postgreSQL on your computer
Open pgadmin -> create db with name challenge-accepted
Put your password and username into backend/src/db/local.env !
