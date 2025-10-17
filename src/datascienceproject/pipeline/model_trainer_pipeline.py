from src.datascienceproject.config.configuration import ConfigurationManager
from src.datascienceproject.components.model_trainer import ModelTrainer
from src.datascienceproject import logger
import os

STAGE_NAME="Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_training(self):
        try:
            config=ConfigurationManager()
            model_trainer_config=config.get_model_trainer_config()
            model_trainer=ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e
