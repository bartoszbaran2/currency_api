
[![Test coverage](https://img.shields.io/badge/coverage-90.97%25-green)](https://choosealicense.com/licenses/mit/)<space><space>
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)<space><space>
[![Packaging](https://img.shields.io/badge/packaging-poetry-blue)](https://python-poetry.org/)<space><space>
[![Framework Django](https://img.shields.io/badge/framework-django-green)](https://www.djangoproject.com/)<space><space>
[![AGPL License](https://img.shields.io/badge/license-Beerware-yellow)](https://github.com/bartoszbaran2/url_shortener/blob/master/LICENSE)

# Currency Rate Browser

This application generates currency rate charts using data from table 'A' of the NBP API. When you initially run the app on your local machine, it will fetch the currency rate data starting from 2005 until the current date. A scheduled task is also set up to fetch the latest data every day at 12:16. This timing aligns with the API's daily update, which occurs between 11:45 and 12:15.



## Demo

### Select start date
![Start Date Selection](https://github.com/bartoszbaran2/currency_api/blob/CA-003_readme/readme_media/start_date.gif?raw=true)

### Select end date
![End Date Selection](https://github.com/bartoszbaran2/currency_api/blob/CA-003_readme/readme_media/end_date.gif?raw=true)

### Select one currency ...
![Currency Selection](https://github.com/bartoszbaran2/currency_api/blob/CA-003_readme/readme_media/one_currency.gif?raw=true)

### or multiple currencies
![Multiple Currency Selection](https://github.com/bartoszbaran2/currency_api/blob/CA-003_readme/readme_media/multiple_currencies.GIF?raw=true)

## Tech Stack

**Server:** Python, Django, Docker, Pytest, Postgres, Celery


## Run Locally

Clone the project

```bash
  git clone git@github.com:bartoszbaran2/currency_api.git
```

Go to the project directory

```bash
  cd nbp_currency_api
```

[Instructions to fill Environment Variables](#environment-variables)
```bash
  cp ./envs/backend.default.env ./envs/backend.env
  cp ./envs/postgres.default.env ./envs/postgres.env
  # set variable values
```

Start the server

```bash
  docker compose up
```

**The migration for fetching the data might take some time since it is making requests for data since 2 january 2005, and there is a 93 days limit in the NBP API.**

## Environment Variables

To run this project, you will need to add the following environment variables to your ./envs/api.env file

```dotenv
DJ_SECRET_KEY= # Django Secret Key for CSRF link
DJ_DEBUG= # Production development mode
DJ_ALLOWED_HOSTS= # Allowed Hosts for Django

LOGGING_LVL= # Python logging package levels

DJ_SU_NAME= # Default superusername
DJ_SU_EMAIL= # Default superuser email
DJ_SU_PASSWORD= # Default superuser password
```

Postgres variables ./envs/postgres.env

```dotenv
POSTGRES_USER= # Postgres root user
POSTGRES_PASSWORD= # Postgres root password
POSTGRES_DB= # Database name
POSTGRES_HOST= # Database host: set to docker compose swervice name
POSTGRES_PORT= # Database port

DB_CONNECTION_STRING=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```
## Coverage report

![Coverage report](https://github.com/bartoszbaran2/currency_api/blob/CA-003_readme/readme_media/Screenshot%20from%202023-08-03%2020-56-16.png?raw=true)


## Author

- [@bartoszbaran2](https://github.com/bartoszbaran2)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/bartoszbaran2?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bartosz-baran-9484a7235/)
