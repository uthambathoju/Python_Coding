import pandas as pd
import numpy as np


#create boolean column based on missing data
def is_val_present(df, boolean_dict):
    """
    :param df : pandas dataframe with train/test data
    :param boolean_dict: dictionary 
    :return: dataframe with new features
    """
    for col_name, new_col in boolean_dict.items():
        df[new_col] = np.where(df[col_name].isnull(), 0, 1)
    return df        

#aggregate count based on col_name
def agg_count(df, agg_dict, col_name='ACCOUNT NUMBER'):
    """
    :param df : pandas dataframe with train/test data
    :param agg_dict : dictionary
    :return: dataframe with new features
    """
    for ctr_col, new_col in agg_dict.items():
        grped_dict = df.groupby(col_name)[ctr_col].nunique().to_dict()
        df[new_col] = df[col_name].map(grped_dict)
    return df

#object to datetime conversion
def convert_to_datetime(df , col_list):
    """
    :param df : pandas dataframe with train/test data
    :param col_list : List with date values
    :return: dataframe with new features
    """
    for col_name in col_list:
        df[col_name]=pd.to_datetime(df[col_name])
    return df

#boolean col based on app_type
def get_app_crt_date(df, col_name='IS_APP_CT_DT'):
    """
    :param df: pandas dataframe
    :return df: df with new features
    """
    df[col_name] = 'OTHER'
    for idx, row in df.iterrows():
        if row['APPLICATION TYPE'] == 'RENEW':
            if pd.isna(row['APPLICATION CREATED DATE']):
                df.at[idx, col_name] = 'NORMAL'
            else:
                df.at[idx, col_name] = 'SUSPECT'
        else:
            df.at[idx, col_name] = 'OTHER'    
    return df

#boolean col based on app_type
def get_app_req_date(df, col_name='IS_APP_REQ_DT'):
    """
    :param df: pandas dataframe
    :return df: df with new features
    """
    df[col_name] = 'OTHER'
    for idx, row in df.iterrows():
        if row['APPLICATION TYPE'] == 'RENEW':
            if pd.isna(row['APPLICATION REQUIREMENTS COMPLETE']):
                df.at[idx, col_name] = 'SUSPECT'
            else:
                df.at[idx, col_name] = 'NORMAL'
        else:
            df.at[idx, col_name] = 'OTHER'    
    return df

#is owner in debt?
def is_debt_col(df, col_name='is_debt'):
    """
    :param df: pandas dataframe with train/test data
    :return df: df with new features
    """
    df[col_name] = 0
    for idx, row in df.iterrows():
        if pd.isna(row['LICENSE APPROVED FOR ISSUANCE']):
            df.at[idx, col_name] = 1
        else:
            df.at[idx, col_name] = 0
        
    return df

#day gap b/w process
def get_diff_days(df, diff_dict):
    """
    :param df: pandas dataframe with train/test data
    :param diff_dict: dictionary
    :return df: df with new features
    """
    for dtcol_1, dtcol_2 in diff_dict.items():
        new_col = f'delta_{dtcol_1}'
        df[new_col] = df[dtcol_1] - df[dtcol_2]
        df[new_col] = df[new_col].fillna('0 days')
        #df[new_col] = df[new_col].fillna(int(float(str('0 days'))))
        df[new_col] = df[new_col].astype(str)
        df[new_col] = df[new_col].map(lambda x: x[:-5])
    return df

#relevance check b/w cols    
def is_name_real(df, col_name='IS_LGL'):
    """
    :param df: pandas dataframe with train/test data
    :return df: df with new features
    """
    df[col_name] = 0
    for idx, row in df.iterrows():
        if row['LEGAL NAME'] == row['DOING BUSINESS AS NAME']:
            df.at[idx, col_name] = 0
        else:
            df.at[idx, col_name] = 1
    return df    


#misclleanous
def convert_coltoint(df , col_list):
    """
    :param df: pandas dataframe with train/test data
    :return df: df with conversion cols
    """
    for col in col_list:
        df[col] = df[col].astype(int)

#misclleanous        
def conver_coltocat(df, col_list):
    """
    :param df: pandas dataframe with train/test data
    :return df: df with conversion cols
    """
    for col in col_list:
        df[col] = pd.Categorical(df[col])

#imputation        
def impute_col(df, col_list):
    """
    :param df: pandas dataframe with train/test data
    :return df: df with imputed cols
    """
    for col in col_list:
        df[col] = df[col].fillna(df[col].mode()[0])
