# 🎬 IMDB Extended ETL Analysis

> **Turning raw movie data into actionable insights through robust Data Engineering.**

Welcome to the **IMDB ETL Project**. This repository hosts an end-to-end Extract, Transform, and Load (ETL) pipeline designed to process IMDB movie records, clean inconsistencies, and structure the data for analytics. Whether you're a data enthusiast or a developer, this project serves as a practical example of handling real-world dirty data with Python and SQL.

---

## 🚀 Project Overview

Data in the real world is messy. This project takes a raw dataset of IMDB movies and puts it through a rigorous cleaning process before storing it in a relational database for querying.

**The Pipeline Flow:**
1.  **Extract 📥**: Ingest raw movie data from `imdb_movies.csv`.
2.  **Transform ⚙️**: 
    *   **Deduplication**: Intelligently identifies and removes duplicate entries based on Title and Release Year, keeping the highest-rated version.
    *   **Surrogate Keys**: Generates unique identifiers for records with missing IDs.
    *   **Data Imputation**: Fills missing ratings using genre-specific or global averages, ensuring no data point is wasted.
    *   **Normalization**: Standardizes data formats for seamless database integration.
3.  **Load 💾**: Pushes the refined dataset into a **MySQL** database (`imdb_analysis` DB, `movies` table) for persistent storage and advanced SQL querying.

---

## 🛠️ Tech Stack & Prerequisites

Before you run this pipeline, ensure you have the following tools installed:

*   **Python 3.x**: The engine running the logic.
*   **MySQL Server**: The destination for our cleaned data.
*   **Jupyter Notebook**: For interactive execution and visualization.
*   **Key Python Libraries**:
    *   `pandas` (Data manipulation)
    *   `sqlalchemy` (Database ORM)
    *   `mysql-connector-python` (MySQL driver)
    *   `matplotlib` (Visualizations)

---

## 📂 Repository Structure

| File | Description |
| :--- | :--- |
| **`IMDB_etl.ipynb`** | 🧠 **The Brain**: The main Jupyter Notebook containing the full ETL logic, data cleaning steps, and visualization cells. |
| **`load_data.py`** | 🔌 **The Loader**: A standalone Python script for quick data loading into MySQL without the interactive elements. |
| **`imdb_ddl.sql`** | 🏗️ **The Blueprint**: SQL script to set up the `imdb_analysis` database and the `movies` table schema. |
| **`imdb_movies.csv`** | 📄 **The Source**: The raw, unprocessed dataset containing movie details. |

---

## ⚡ How to Run

### 1. Database Setup
First, prepare your MySQL environment. You can use the provided SQL script to create the necessary database and table structure.
```sql
-- Run the contents of imdb_ddl.sql in your MySQL Workbench or CLI
source imdb_ddl.sql;
```

### 2. Configure Credentials
Open `IMDB_etl.ipynb` or `load_data.py` and update the database connection string with your local MySQL credentials:
```python
# Look for this line and update 'user' and 'password'
engine = create_engine("mysql+mysqlconnector://root:YOUR_PASSWORD@localhost:3306/imdb_analysis")
```

### 3. Execute the Pipeline
You have two options:
*   **Interactive Mode**: Open `IMDB_etl.ipynb` in Jupyter/VS Code and run all cells to see the step-by-step transformation and final visualizations.
*   **Batch Mode**: Run the python script for a direct load.
    ```bash
    python load_data.py
    ```

---

## 📊 Sample Insights
Once the data is loaded, you can run powerful queries. The notebook includes examples such as:
*   *Top 10 High-Grossing Movies per Year* (Visualized)
*   *Average Rating Distribution by Genre*

---

## 🤝 Contribution
Found a better way to handle missing values? Want to add more visualizations? Pull requests are welcome! 

1.  Fork the Project
2.  Create your Feature Branch
3.  Commit your Changes
4.  Open a Pull Request

---

*Crafted with ❤️ by Manan*
