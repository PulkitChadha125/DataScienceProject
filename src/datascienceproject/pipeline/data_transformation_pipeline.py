from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.data_tranformation import DataTransformation
from src.datascienceproject import logger
from pathlib import Path
import os

STAGE_NAME="Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
                logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
            else:
                logger.info(f">>>>>> stage {STAGE_NAME} skipped <<<<<<")
                raise Exception("Data transformation failed")
        except Exception as e:
            print(e)
            raise e
 