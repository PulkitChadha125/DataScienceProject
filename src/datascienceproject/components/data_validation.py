from src.datascienceproject import logger

from src.datascienceproject.entity.config_entity import (DataValidataionConfig,DataIngestionConfig)
import pandas as pd

class DataValidation:
    def __init__(self,config:DataValidataionConfig):
        self.config=config
    
    def validate_all_columns(self)->bool:
        try:
            validation_status=None
            data=pd.read_csv(self.config.unzip_data_dir)
            all_cols=list(data.columns)
            all_schema=self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise e
    
    def validate_datatype(self)->bool:
        try:
            import numpy as np
            validation_status=True
            data=pd.read_csv(self.config.unzip_data_dir)
            all_schema=self.config.all_schema  # dict: {column_name: "float"|"int"}
            
            for col_name, expected_type in all_schema.items():
                if col_name not in data.columns:
                    validation_status=False
                    continue
                expected_str = str(expected_type).lower()
                if expected_str == 'float':
                    data[col_name] = data[col_name].astype(float)
                elif expected_str == 'int':
                    data[col_name] = data[col_name].astype(int)
                # ignore other types for now
            
            return validation_status
        except Exception as e:
            raise e
    