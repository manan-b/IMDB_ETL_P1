# IMDB Movie Dataset Analysis

I built this project to analyze IMDB movie data by creating an ETL pipeline. The idea is to take raw data, clean it up, and store it in a database so I can run queries on it later.

It handles things like removing duplicates, filling in missing ratings, and making sure the data types are correct before pushing everything to MySQL.

## Prerequisites
You'll need Python installed along with a MySQL server running locally.
Libraries used:
- pandas
- sqlalchemy
- mysql-connector-python
- matplotlib

## How to use
1. First, create the database and table. I've included a file named `imdb_ddl.sql` that you can run in your MySQL workbench.
2. Open up `IMDB_etl.ipynb` or `load_data.py`. You will need to change the database password to whatever you have set up on your machine.
3. Run the notebook or the script. It will read the csv, process it, and insert the rows into the `movies` table.

## Files
- `IMDB_etl.ipynb`: This has the core logic and some charts I made to visualize the data.
- `load_data.py`: Just the loading script if you don't want to open the notebook.
- `imdb_ddl.sql`: SQL script for the database schema.
- `imdb_movies.csv`: Raw data source.

That's pretty much it. Let me know if you run into issues.
