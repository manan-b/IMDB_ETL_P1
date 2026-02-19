# IMDB Movie Dataset Analysis 🎬📊

## Project Overview
This project delivers an end-to-end data analysis pipeline for IMDB movie data, utilizing Python for ETL and SQL for structured querying. The workflow transforms raw movie data into actionable insights through a series of cleaning, imputation, and visualization steps.

The primary objective is to extract meaningful trends regarding movie financials, genre popularity, and talent performance (directors/actors) to understand the drivers of industry success.

## Datasets Used
The project relies on two main components to manage and store information:
- `imdb_movies.csv`: Raw dataset containing movie metadata (titles, genres, ratings, budgets, gross, etc.).
- `imdb_ddl.sql`: Database schema definition optimized for movie analysis in MySQL.

## Tech Stack
- **Python**: Core logic and automation.
- **Pandas & NumPy**: Data manipulation and statistical imputation.
- **MySQL & SQLAlchemy**: Relational storage and database integration.
- **Matplotlib**: Data visualization and graphical reporting.
- **Jupyter Notebook**: Interactive analysis and prototyping.

## ETL Workflow
I structured the ETL process to ensure data integrity before any analysis was performed:
1. **Extraction**: Raw CSV files are ingested using Pandas for initial inspection.
2. **Data Cleaning & Processing**:
    - **Deduplication**: Handled duplicates by movie title and release year, retaining records with superior ratings.
    - **Missing Value Imputation**: Applied genre-specific logic (averages for ratings, medians for budgets) to fill gaps accurately.
    - **Normalization**: Standardized categorical fields like director names and actors (handling 'Unknown' values).
3. **Database Loading**: Cleaned data is loaded into a MySQL database via SQLAlchemy to support high-performance SQL analytics.

## Dashboards & Analysis 
The analysis is categorized into four key areas of focus:
- **Dashboard 1: Financial Performance**: Analysis of revenue streams, including the top 10 highest-grossing movies per year.
- **Dashboard 2: Genre Insights**: Examining the distribution of quality (ratings) across different movie categories.
- **Dashboard 3: Personnel Analytics**: Identifying the top 5 directors based on consistent audience rating performance.
- **Dashboard 4: Industry KPIs**: Investigating business correlations, such as the relationship between production budget and gross revenue.

---
*Developed for IMDB Data Science Analysis.*