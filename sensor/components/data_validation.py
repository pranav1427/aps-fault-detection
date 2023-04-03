from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
from scipy.stats import ks_2samp
import pandas as pd
from typing import Optional




class DataValidation:


    def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'20} Data Validation {'<<'*20}")
            self.data_validation_config= data_validation_config
            self.validation_error=dict()
        except Exception as e:
            raise SensorException(e,sys)

   

    def drop_missing_values_columns(self,df,)->pd.DataFrame:
        """
        This function will drop column which contains missimg value more then specified threshold
        df:accepts a pandas dataframe
        threshold: percantage criteria to drop a column
        ====================================================================================
        returns pandas dataframe is atleast a single column is available after missing column drops
        """


    
        try:
            threshold= self.data_validation_config.missing_threshold
            null_report =df.isna().sum()/df.shape[0]
            # selecting colnum name  which contains null values
            drop_column_names = null_report[null_report>threshold].index

            self.validation_error["dropped_columns"]=drop_column_names
            df.drop(list(drop_column_names),axis=1,inplace=True)

            # return none if no columns left
            if len(df.columns)==0:
                return none
        except Exception as e:
            raise SensorException(e,sys)
    
    def is_required_columns_exists(self,base_df:pd.DataFrame,current_df:pd.DataFrame)->bool:
        try:
            base_columns=base_df.columns
            current_columns=current_df.columns

            missing_columns = []
            for base_column in base_columns:
                if base_column not in current_columns:
                    missing_columns.append(base_column)

            if len(missing_columns)>0:
                self.validation_error["missing_column"]=missing_columns
                return False
        except Exception as e:
            raise SensorException(e,sys)

    def data_drift(self,base_df:pd.DataFrame,current_df:pd.DataFrame):
        try:
            drift_report=dict()
            base_columns=base_df.columns
            current_columns=current_df.columns

            for base_column in base_columns:
                base_date,current_data = base_df[base_column],current_df[base_column]
                # null hypothesis is that both column data drawn from same distribution
                same_distribution=ks_2samp(base_date,current_data)
                
                if same_distribution.pvalue>0.05:
                    # we are accepting null hypothesis
                    drift_report[base_column]={
                        "pvalues":same_distribution.pvalue,
                        "same_distribution":True
                    }
                
                else:
                    drift_report[base_column]={
                        "pvalues":same_distribution.pvalue,
                        "same_distribution":False
                    }
                    #different distribution

        except Exception as e:
            raise SensorException(e,sys)
        

    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        pass