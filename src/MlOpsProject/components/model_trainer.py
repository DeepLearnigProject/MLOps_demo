import pandas as pd
import os

from sklearn.linear_model import ElasticNet
import joblib
from src.MlOpsProject import logger
from src.MlOpsProject.config.configuration import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        try:
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)
            logger.info("training data reading : successful")
            train_x = train_data.drop([self.config.target_column], axis=1)
            test_x = test_data.drop([self.config.target_column], axis=1)
            train_y = train_data[[self.config.target_column]]
            test_y = test_data[[self.config.target_column]]
            logger.info("training started ..")
            lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
            lr.fit(train_x, train_y)
            logger.info("training  : successfull")
            logger.info("Saving model started ")
            joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
            logger.info("Saving model : successfull")
        except Exception as e:
            logger.error(f"Error in training : \n {e}")