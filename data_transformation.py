import yaml
import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import psycopg2
import numpy
import re
from datetime import datetime
import datetime as dt

class DataTransform:

    def format_date(self, data, column_name):
        data[column_name] = pd.to_datetime(data[column_name], format='%b-%Y')

        return data
           
    
    def remove_non_numbers(self, data, column_name):
        # Extract numeric part using regular expression
        data[column_name] = data[column_name].astype(str).str.extract('(\d+)', expand=False)

        return data
    
    def column_to_int(self, data, column_name):
        data[column_name] = data[column_name].astype('Int64')
        return data
    

