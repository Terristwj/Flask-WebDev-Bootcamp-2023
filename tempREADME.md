# Full Stack WebApp Project

| Frontend  | Backend | Bridge | Package Managers |
| :-------: | :-----: | :----: | :--------------: |
|  Vue.js   |  Flask  | Axios  |       node       |
| Bootstrap |         |        |       pip        |

---

## Udemy Courses

<style>
   .cert{
      display: block;
      margin:auto;
      width:60%;
   }
</style>

### [1. Vue - The Complete Guide (incl. Router & Composition API)](https://www.udemy.com/course/vuejs-2-the-complete-guide/)

- [[By Maximilian Schwarzmüller]](https://www.udemy.com/user/maximilian-schwarzmuller/)

<img src="https://rsham.co.id/wp-content/uploads/2021/03/image-placeholder.jpg" class="cert">

### [2. Bootstrap 5 Course - The Complete Guide Step by Step (2023)](https://www.udemy.com/course/the-complete-bootstrap-5-course-for-beginners-step-by-step/)

- [[By Fatah Gabrial]](https://www.udemy.com/user/fatahgabrial/)

<img src="https://rsham.co.id/wp-content/uploads/2021/03/image-placeholder.jpg" class="cert">

### [3. Web Developer Bootcamp with Flask and Python in 2023](https://www.udemy.com/course/web-developer-bootcamp-flask-python/)

- [[By Jose Salvatierra]](https://www.udemy.com/user/josesalvatierra/)

<img src="https://rsham.co.id/wp-content/uploads/2021/03/image-placeholder.jpg" class="cert">

---

## Tutorial

- [Full Stack Project with Vue.js and Flask (Games Library App)](https://www.youtube.com/watch?v=lenV5aVOMp8)
  - [[By Bek Brace]](https://www.youtube.com/@BekBrace)

### Vue-Flask SPA Plan

1.  Connect UI front-end app to Flask back-end server. (Axios)
2.  Develop a RESTful API with Flask.
3.  Use Vue router to create routes.
4.  Bootstrap for styling and for 2 modals.

### Application Tools:

1. Vue v2.6.11
2. Vue CLI v4.5.11
3. Node v15.7.0
4. npm v7.4.3
5. Flask v1.1.2
6. Python v3.9

---

## Running the project

Terminal 1

```bash
   cd frontend
   npm install -g @vue/cli
   npm install --save-dev eslint eslint-plugin-vue
```

Terminal 2

```bash
   cd frontend
   npm install -g @vue/cli
   npm install --save-dev eslint eslint-plugin-vue
```

---

## Getting Started with Vue.js

### Instructions

1. Installed Node.js
2. Install vue.js
   ```bash
   cd frontend
   npm install -g @vue/cli
   npm install --save-dev eslint eslint-plugin-vue
   ```
3. VSCode extensions
   - [Vue Language Features (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
   - [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
4. Create Vue project
   ```bash
   vue create frontend
   # Manually select features
   # Babel, Router, Linter / Formatter
   # v2.x
   # Prettier
   # Lint on save
   # package.json
   ```
5. Run Vue project
   ```bash
   cd frontend
   npm run serve
   ```
6. [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

   ```html
   <!-- BootStrap CSS -->
   <link
     href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
     rel="stylesheet"
   />

   <!-- BootStrap popper JS -->
   <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.7/dist/umd/popper.min.js"></script>
   <!-- BootStrap JS -->
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
   ```

---

## Getting Started with Flask

### Prerequisites

1. Latest Python (Currently Py3)
2. Create/Activate Python environment
   - **Note:** Default env is your system default
   ```bash
   cd backend
   py -3 -m venv .venv
   source .venv/Scripts/activate # Mac does not need "source"
   ```
3. Install dependancies

   ```bash
   pip install -r requirements.txt
   ```

### Running the Project (Windows)

1. Always set Python env when opening VSCode
2. Run deployment server
   ```bash
   source .venv/Scripts/activate # Mac does not need "source"
   python main.py
   ```
3. Copy/Paste URL into browser

### CLI debugging commands:

```bash
# Pip
pip -V   # Shows current working envrinoment
pip list # Displays every installed dependancies
pip install <name> # install <name> dependancy
pip uninstall <name> # Uninstall <name> dependancy
pip install -r requirements.txt # install recursively
pip uninstall -r requirements.txt # Uninstall recursively

# Flask
source .venv/Scripts/activate
export FLASK_DEBUG=1  # Sets run to debug
flask run # Run deployment
flask --debug run # Run deployment with debugger

# Python
source .venv/Scripts/activate
python main.py
```

---
