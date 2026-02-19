# IMDB Movie Dataset Analysis

## Project Overview
This project delivers a comprehensive data analysis pipeline for the IMDB movie dataset. It utilizes Python for the extraction, transformation, and loading (ETL) process and SQL for advanced data querying. The goal is to convert raw data into structured insights regarding the film industry's performance.

The primary objective is to evaluate financial success, audience reception across genres, and the effectiveness of key talent such as directors, helping identify what truly drives impact in cinema.

## Datasets Used
The analysis is based on the following resources:
- `imdb_movies.csv`: A detailed collection of movie metadata including financial figures, ratings, and production details.
- `imdb_ddl.sql`: The schema definition used to establish a robust MySQL environment for the analysis.

## Tech Stack
- **Python**: Facilitates automation and core data logic.
- **Pandas & NumPy**: Essential for data manipulation and statistical processing.
- **MySQL & SQLAlchemy**: Powers relational storage and database management.
- **Matplotlib**: Used for generating clear visual insights.
- **Jupyter Notebook**: Serves as the primary environment for experimentation and analysis.

## ETL Workflow
The data was put through a rigorous cleaning process to ensure accuracy and reliability:
1. **Extraction**: Raw data is pulled from CSV files using Pandas for initial review.
2. **Data Cleaning & Processing**:
    - **Deduplication**: Records are filtered based on the combination of title and release year, ensuring only the highest-rated versions are retained.
    - **Missing Value Imputation**: Strategically filled gaps in the data using averages for ratings and medians for budgets, specific to each genre.
    - **Normalization**: Standardized various fields, including director and actor names, to maintain consistency.
3. **Database Loading**: The processed data is migrated to a MySQL database using SQLAlchemy to enable efficient SQL-driven reporting.

## Dashboards & Analysis 
The analysis interprets the data through four specialized lenses:
- **Dashboard 1: Historical Financial Performance**: Highlights the top 10 highest-grossing movies for each year to track industry growth over time.
- **Dashboard 2: Genre Quality Assessment**: Visualizes the distribution of average ratings across genres to see which categories consistently appeal to audiences.
- **Dashboard 3: Director Achievement Analysis**: Ranks the top 5 directors based on their average movie ratings, identifying consistent excellence in storytelling.
- **Dashboard 4: Investment vs. Return Correlation**: A statistical look at the relationship between production budgets and gross revenue to evaluate financial risk and reward.

---