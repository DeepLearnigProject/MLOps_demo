import os
import urllib.request as request
import zipfile
from src.MlOpsProject import logger
from src.MlOpsProject.utils.common import get_size
from pathlib import Path
import sqlite3
import pandas as pd
from src.MlOpsProject.config.configuration import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def create_database(self):
        # read the pandas csv as pandas dataframe
        df = pd.read_csv(self.config.dataset_csv_file_path)
        # Create a connection to the SQLite database
        conn = sqlite3.connect(self.config.database_name)
        # Create a cursor object
        cursor = conn.cursor()
        # Create the table in the SQLite database with the same schema as the CSV header
        create_table_query = f'CREATE TABLE IF NOT EXISTS {self.config.tabel_name} {tuple(df.columns)}'
        cursor.execute(create_table_query)

        # Insert the data from the DataFrame into the SQLite table
        df.to_sql(self.config.tabel_name, conn, if_exists='replace', index=False)

        # Commit changes and close the database connection
        conn.commit()
        conn.close()
        logger.info(f"CSV data loaded into the '{self.config.tabel_name}' table in the '{self.config.database_name}' database.")

    def extract_data(self):
        # Create a connection to the SQLite database
        conn = sqlite3.connect(self.config.database_name)
        # Query to select all rows from the table
        query = f"SELECT * FROM {self.config.tabel_name};"
        # Read the table into a Pandas DataFrame
        df = pd.read_sql_query(query, conn)
        # Close the database connection
        conn.close()
        # Display the DataFrame
        logger.info(f"dataframe.shape : {df.shape}")
        logger.info(f"dataframe.column : { df.columns}")
        return df

    def inset_df_into_table(self,df):
        """
        Insert a Pandas DataFrame into an SQLite table.

        Parameters:
        - df: Pandas DataFrame containing the data to be inserted.
        - table_name: Name of the SQLite table where data will be inserted.
        - db_filename: Filename of the SQLite database (default is 'dataset.db').
        """
        try:
            # Create a connection to the SQLite database
            conn = sqlite3.connect(self.config.database_name)

            # Use the Pandas to_sql method to insert the DataFrame into the table
            df.to_sql(self.config.extract_table_name, con=conn,if_exists='replace', index=False)
            logger.info(f"Data inserted into '{self.config.extract_table_name}' table in '{self.config.database_name}' database.")
        except Exception as e:
            logger.error(f"Error: {e}")
        finally:
            # Close the database connection
            conn.close()



