<h1 align="center">Takagi</h1>

![Deploy - Frontend](https://github.com/RangerDigital/takagi/workflows/Deploy%20-%20Frontend/badge.svg?branch=master)
![Build - Production](https://github.com/RangerDigital/takagi/workflows/Build%20-%20Production/badge.svg?branch=master)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Source of **Takagi**, simple web application build with **Flask** and **Vue.js** used to conduct quick, anonymous polls over the internet.

**Takagi** was built as a university web development course project,  
That means it's simpler than It should be, to be considered a production app!

<br>

## 💻 Running Locally

**It's easy to get going with developing Takagi!**

This project uses **Docker** as a development and production deployment tool, so **you need It** first!

### # Backend Setup
> 🔥 Execute every command in `./backend` directory!

**If you only want to run It**, you need to:
- Spin up the whole stack as containers, simply type: 
`docker-compose up -d`

This will spin up all the necessary containers and expose Takagi service **API** at `http://127.0.0.1:5000`.

---
But if **you want to make changes** to the **Flask** app, you need to:
-   Install **Python 3.8**, then projects requirements.
`pip3 install -r requirements.txt`

-   Also, It's *optionally* development requirements.
`pip3 install -r dev-requirements.txt`

-   After that spin up **Redis** and **MongoDB** as containers.
`docker-compose up -d redis mongo`

-   Run `main.py`, entry point for Flask app.
`python3 ./main.py`

This will spin up databases, and run Python code with the development server at `http://127.0.0.1:5000`.

### # Frontend Setup
> 🔥 Execute every command in `./frontend` directory!

If **you want to make changes** to the **Vue.js** app, you need to:
-   Install **NPM**, then projects requirements.
`npm install`

-   To then serve a website, simply type:
`npm run serve`

This will create a development web server at `http://127.0.0.1:8080`.
And It's a lot simpler!

<br>

## 🚧 Contributing

**You are more than welcome to help me improve Takagi!**

Just fork this project from the `master` branch and submit a Pull Request (PR).
If you are modifying backend you should also run `pytest` functional tests inside `backend/tests` directory.

<br>

## 📃 License
This project is licensed under [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) .