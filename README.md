# Web Developer Bootcamp with Flask and Python in 2023

> Udemy Paid Course

---

## ![Certificate](https://rsham.co.id/wp-content/uploads/2021/03/image-placeholder.jpg)

---

## Getting Started with Flask

### Prerequisites

1. Latest Python (Currently Py3)
2. Create/Activate Python environment
   - **Note:** Default env is your system default
   ```bash
   py -3 -m venv .venv
   source .venv/Scripts/activate
   export FLASK_DEBUG=1
   ```

### Dependancies

1. [Flask](https://code.visualstudio.com/docs/python/tutorial-flask)
   ```bash
   pip install Flask
   ```
2. [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

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

### Running the Project (Windows)

1. Always set Python env when opening VSCode
   ```bash
   source .venv/Scripts/activate
   export FLASK_DEBUG=1
   ```
2. Run deployment server
   ```bash
   flask run
   ```
3. Run deployment server w/ debug mode
   ```bash
   flask --debug run # Enables data reloading
   ```
4. Copy/Paste URL into browser

### Running the Project (Mac)

1. Someone else please edit here, i dont use Mac 😔

### Beginner's Note:

1. It is best practice to download all dependancies locally onto this project
   - Pip debugging commands:
     ```bash
     # Pip
     pip -V   # Shows current working envrinoment
     pip list # Displays every installed dependancies
     pip uninstall <name> # Uninstall <name> dependancy

     # Flask
     flask run # Run deployment
     flask --debug run # Developing
     ```

---

## Starting a Project (VSCode - Windows)

(If you want to practice separately)

1. Create your own workspace
2. In VSCode, create a new bash terminal
3. Create Python environment
   ```bash
   py -3 -m venv .venv
   ```
4. Activate virtual envrionment
   ```bash
   source .venv/Scripts/activate
   export FLASK_DEBUG=1
   ```
5. Install Flask
   ```bash
   pip install Flask
   ```
6. Create app.py in root directory
7. Start coding
8. Run server using
   ```bash
   flask run
   flask --debug run
   ```

---
