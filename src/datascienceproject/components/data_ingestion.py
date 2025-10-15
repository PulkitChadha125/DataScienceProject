from src.datascienceproject import logger
from urllib import request
import os
import zipfile
from src.datascienceproject.entity.config_entity import (DataIngestionConfig)



class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    # downloading zip file from github link in config.yaml file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"file: {filename} downloaded with following info: {headers}")
        else:
            logger.info(f"file already exists of size")
    
    # extract zipfile
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
    

    

   
        
            