# 📒 NoteIt

A simple and modular backend project built with Python. This project contains application logic, configuration, and test suites, organized for maintainability and scalability.

---

## 📁 Project Structure

├── .env                   <- Environment variables file
├── .gitignore             <- Specifies files and directories to ignore in Git
├── README.md              <- Top-level README for the project
├── requirements.txt       <- Dependencies required to run the project
├── config.py              <- Global configuration settings used throughout the project
├── pytest.ini             <- Configuration file for pytest
│
├── app                    <- Core application logic
│   ├── __pycache__        <- Compiled Python cache files
│   ├── database.py        <- Handles database connections and operations
│   ├── deps.py            <- Dependency injections or shared resources
│   └── main.py            <- Entry point for the application
│
├── .github                <- GitHub workflows or templates (CI/CD, issue templates, etc.)
│
├── noteit_                <- Package or module source directory
│
├── myenv                  <- Virtual environment directory (should be excluded from version control)
│
├── tests                  <- Unit and integration tests
│   ├── __pycache__        <- Compiled Python cache files
│   └── test_data.py       <- Test scripts for validating data or logic
│
├── __pycache__            <- Root-level cache directory (ignore in version control)
├── .pytest_cache          <- Pytest's internal cache directory (can be ignored)


---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

###  📦 Clone the Repository
```bash
git clone https://github.com/your-username/NoteIt.git
cd NoteIt
```

### 🐍 Create a Virtual Environment

You can use `venv` or any other virtual environment manager like `conda`.

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 📦 Install Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### ⚙️ Set Up Environment Variables

Create a `.env` file in the root directory and add your MySQL database configuration and secret key:

```
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/databasename
SECRET_KEY=your-secret-key
```
- Replace username, password, and databasename accordingly.

- pymysql must be installed (pip install pymysql) — make sure it's in requirements.txt.

### 🚀 Run the Application

Run the backend server using uvicorn:

```bash
uvicorn app.main:app --reload
```

- Open in browser: http://localhost:8000

- Swagger UI will be at: http://localhost:8000/docs

### 🧪 Run Tests
Use pytest to run the test suite:

```
pytest
```
Make sure:
- You're in the virtual environment.
- Test files are named with the test_*.py format.
- The pytest.ini file (if present) is configured properly.

---

### 🌟 How the 12-Factor App Methodology is Applied

This project follows the [12-Factor App](https://12factor.net/) principles to ensure best practices for building scalable, maintainable, and portable applications.

Here’s how the key factors are implemented:

1. **Codebase**  
   Single codebase tracked in Git (`git clone`).

2. **Dependencies**  
   Explicitly declared in `requirements.txt` and installed in isolated virtual environments (`venv`).

3. **Config**  
   Configuration is stored in environment variables (`.env` file), not in code.  
   Example: `DATABASE_URL`, `SECRET_KEY` in `.env`.

4. **Backing Services**  
   External services like MySQL database are treated as attached resources, configurable via environment variables.

5. **Build, Release, Run**  
   Build stage installs dependencies, release stage prepares configuration, and run stage starts the server (`uvicorn app.main:app`).

6. **Processes**  
   The app runs as one or more stateless processes, with no data stored locally between requests.

7. **Port Binding**  
   The app is self-contained and exports services by binding to a port (e.g., 8000) using Uvicorn.

8. **Concurrency**  
   Processes can be scaled horizontally by running multiple instances behind a load balancer (managed outside the code).

9. **Disposability**  
   Fast startup and graceful shutdown with `uvicorn --reload` for fast dev iteration.

10. **Dev/Prod Parity**  
    Similar environment setup between development and production by using environment variables and Docker (can be used).

11. **Logs**  
    The app writes logs to stdout/stderr, letting the execution environment capture and manage them.

12. **Admin Processes**  
    One-off administrative or maintenance tasks (like database migrations) can be run as separate processes.

---

By following these principles, this project ensures consistency, portability, and ease of deployment across environments.
