# HR Data Engineering Pipeline 🚀

This project automates the process of setting up a PostgreSQL database and loading HR datasets into it using Docker and Python.

## ✨ Project Overview
- **Infrastructure:** Containerized PostgreSQL 15 database using **Docker Compose**.
- **Data Source:** CSV datasets containing Employees, Departments, and Countries.
- **Automation:** A **Python (Pandas)** script that connects to the database and performs the ETL process (Extract, Transform, Load) into a specific `hr` schema.
- **Persistence:** Configured **Docker Volumes** to ensure data is saved even if the container stops.

## 🛠️ Technologies Used
- **Database:** PostgreSQL
- **Containerization:** Docker & Docker Compose
- **Scripting:** Python 3.12 (Pandas, SQLAlchemy, Psycopg2)
- **Version Control:** Git & GitHub

## 📂 Project Structure
- `docker-compose.yml`: Defines the database service and environment variables.
- `load_data.py`: The Python logic to read CSVs and write them to Postgres.
- `*.csv`: Source data files.
- `README.md`: Project documentation.

## 🚀 How to Run
1. Start the containers:
   ```bash
   docker compose up -d
python load_data.py
