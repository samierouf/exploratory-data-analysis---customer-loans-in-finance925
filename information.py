import pandas as pd
from dataframe_transformtion import DataFrameTransform
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
dftrans = DataFrameTransform()


class DataFrameInfo:

    def is_data_skew(self, data, column_name):
        skew = data[column_name].skew()
        return f'the skew of {column_name} is : {skew}'
      
    def describe_columns_types(self, data):
        return data.info()

    def describe_data(self, data):
        return data.describe(include = 'all')

    def count_distinct_values(self, data):
        distinct_counts = pd.DataFrame(data.apply(lambda x: len(x.unique())))
        return distinct_counts

    def print_shape(self, data):
        return data.shape

    def generate_null_counts(self, data):
        null_counts = data.isnull().sum()
        percentage_nulls = (null_counts / len(data)) * 100
        null_info = pd.DataFrame({'Null Counts': null_counts, 'Percentage Nulls': percentage_nulls})
        return null_info

    def describe_data_type(self, data):
        df = pd.DataFrame()
        df['Column_Name'] = data.columns
        for column in data.columns:
            df.loc[df['Column_Name'] == column, 'Data_Type'] = data[column].dtype
        return df

    def extract_statistics(self, data):
        df_stats = data.describe()
        df_stats = df_stats.loc[['50%', 'std', 'mean']]
        df_stats = df_stats.transpose()
        return df_stats
    
    def count_distinct(self, data):
        df = pd.DataFrame(columns=['Column_Name', 'Distinct_Count'])
        df['Column_Name'] = data.columns
        for column in data.columns:
                df.loc[df['Column_Name'] == column, 'Distinct_Count'] = len(data[column].unique())
        return df

    def compute_vif(self, data, considered_features):
    
        X = data[considered_features]
        # the calculation of variance inflation requires a constant
        X['intercept'] = 1
        # create dataframe to store vif values
        vif = pd.DataFrame()
        vif["Variable"] = X.columns
        vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
        vif = vif[vif['Variable']!='intercept']
        return vif