# 🚀 Sahihi Text Services

This documentation provides instructions for running this 🐳 Dockerized Django application using the provided `docker-compose.yaml` file and associated Dockerfiles. The web application consists of three services:

- A PostgreSQL database(`db`)
- The main app(`frontend`)
- A nginx web server(`nginx`)

## Prerequisites 🛠️

Before proceeding, ensure you have the following installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/)

## Directory Structure 📂

The following is the project directory structure:

                sahihi-text-services/
                |-- Database/
                |   |-- Dockerfile
                |-- nginx/
                |   |-- Dockerfile
                |   |-- default.conf
                |-- docker-compose.yaml
                |-- Dockerfile (frontend)
                |   entrypoint.sh
                |   other_frontend_files
                |-- .env
                |-- requirements.txt
                |-- other_project_files

## Setup ⚙️

1. Clone the repository.
2. Create a `.env` file in the project root and populate with the necessary variables.

    - POSTGRES_DB=your_database_name
    - POSTGRES_HOST=db
    - POSTGRES_USER=your_username
    - POSTGRES_PASSWORD=your_password
    - POSTGRES_HOST_AUTH_METHOD=trust
    - SECRET_KEY=your_secret_key

## Running the Application ▶️
1. Launch the services in detached mode by runninng:
     `docker-compose up -d db`(Database first)
     then:
        `docker-compose up -d`(Other services)

`NB: You can integrate the wait-for-it.sh script since you'll find the app tries to connect to the db before it's ready. This may cause errors. The wait-for-it.sh script can be found [here](https://github.com/vishnubob/wait-for-it). If you opt to do this, please modify the frontend Dockerfile appropriately.` 

## Customization 🧩
- Modify the Database/Dockerfile, ./Dockerfile, and nginx/Dockerfile files to include any extra configurations or dependencies required by your application.
- Personalize the docker-compose.yaml file to add additional services or adjust existing ones according to your project's necessities.
- Modify the Nginx configuration in nginx/default.conf to align with your frontend application's requirements.

## Credits 🙌

The frontend theme is from Start Boostrap [here][https://startbootstrap.com/theme/agency]

## Contributing 📢

If you'd like to contribute, feel free to open a [pull request](https://github.com/kimjoemaina/POS/pulls) and we can collaborate!

## Donate 💰

Buy me a coffee. It'll help me stay motivated! ☕

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=XVNG6ATBXFJAC)\

## Contact 🤙

[LinkedIn](https://www.linkedin.com/in/joemainak/) 🔗

[X](https://x.com/joemainak) ❌