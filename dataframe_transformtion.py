import numpy as np
import pandas as pd
import datetime
from datetime import datetime
from scipy import stats
from scipy.stats import yeojohnson

class DataFrameTransform:

    def remove_columns(self, data, colmns_to_remove):
        colmns_to_remove = colmns_to_remove
        data.drop(colmns_to_remove, axis=1 ,inplace = True)
        return data
    

    def remove_null_rows(self, data, nulls_in_column):
        nulls_in_column = nulls_in_column
        data.dropna(subset=nulls_in_column, inplace=True, how='any')
        return data

    def fix_next_payment_dates(self, data, date_to_fix, previous_date):
        for index in data.index:
            if pd.isnull(data.at[index, date_to_fix]):
                data.at[index, date_to_fix] = data.at[index, previous_date] + pd.DateOffset(months=1)
        return data
    
    def replace_nulls_with_mean(self, data, column_name):
        mean_value = data[column_name].mean()
        data[column_name] = data[column_name].fillna(mean_value)
        return data
    
    def replace_nulls_with_median(self, data, column_name):
        # median_value = data[column_name].median()
        # # data[column_name] = data[column_name].fillna(median)
        # data[column_name].fillna(median_value, inplace=True)
        # return data
        data[column_name] = data[column_name].fillna(data[column_name].median())
        return data
    

    def replace_nulls_with_mode(self, data, column_name):
        mode = data[column_name].mode()
        # Select the first mode value if multiple modes exist
        mode_value = mode[0] if not mode.empty else None
        data[column_name] = data[column_name].fillna(mode_value)
        return data

    def log_transformation(self,data, column_name):
        data[column_name] = data[column_name].map(lambda i: np.log(i) if i > 0 else 0)
        return data
    
    def box_cox_transformation(self, data, column_name):
        boxcox_data = stats.boxcox(data[column_name])# transformed_data, optimal_lambda= stats.boxcox(data[column_name])
        data[column_name] = pd.Series(boxcox_data[0])# boxcox_data[0] transformed_data

        return data
    
    def yeo_johnson_transformation(self, data, column_name):
        yj_data = data[column_name]
        yj_data = stats.yeojohnson(yj_data)# transformed_data, optimal_lambda= stats.yeojohnson(data[column_name])
        data[column_name] = pd.Series(yj_data[0])
        return data
    

    def remove_outliers(self, data, column_name):
        cloumn_mean = np.mean(data[column_name])
        column_std = np.std(data[column_name])
        z_score = (data[column_name] - cloumn_mean) / column_std
        data['z_score'] = z_score
        mask = (data['z_score'] > -3) & (data['z_score'] < 3)
        data = data[mask]

        return data

     

    




