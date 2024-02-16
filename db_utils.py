import yaml
import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import psycopg2
class RDSDatabaseConnector:

    def read_credentials(self):
        '''
        This fucntion reads the credentials.yaml file
        
        Args:
            n/a
        Returns:
            dict: dicionary containg the contents of the credential.yaml file
        '''
        
        with open('credentials.yaml', 'r') as file:
            yaml_creds = yaml.safe_load(file)

        return yaml_creds
    

    def __init__(self):
        self.creds = self.read_credentials()
        self.engine = self.init_db_engine()

    
    def init_db_engine(self):
        """
        fucntion initializes a database engine using the database credentials.

        Args:
            db_creds (dict): Dictionary containing database credentials.

        Returns:
            sqlalchemy.engine.base.Engine: Initialized database engine.
        """
        engine = create_engine(f"postgresql+psycopg2://{self.creds['RDS_USER']}:{self.creds['RDS_PASSWORD']}@{self.creds['RDS_HOST']}:{self.creds['RDS_PORT']}/{self.creds['RDS_DATABASE']}")
        return engine

    def read_rds_table(self, table_name): # table_name = loan_payments
        """
        this function reads data from an RDS database table.

        Args:
            engine: Database engine.
            table_name (str): Name of the table to read.

        Returns:
            pd.DataFrame: DataFrame containing the read data.
        """
        with self.engine.connect() as conn:
            read_data = pd.read_sql_table(table_name, self.engine)
        return read_data   

    def save_to_csv(self, data, file_name):
        data.to_csv(file_name, index=False)
    

    def read_csv_data(self, file_name):
        data = pd.read_csv(file_name)
        return data

    




