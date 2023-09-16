import pandas as pd
import os
from src.MlOpsProject import logger
from src.MlOpsProject.config.configuration import DataPreparationConfig

class DataPreparation:

    def __init__(self,config:DataPreparationConfig):
        self.config = config

    def dataset_drop_column(self):
        try:
            dataset_path = self.config.dataset_path
            dataset = pd.read_csv(dataset_path)
            if self.config.drop_column is not None:
                dataset = dataset.drop(self.config.drop_column,axis=1)

            save_path = os.path.join(self.config.root_dir,'dataset_prepared.csv')
            dataset.to_csv(save_path,index=False)
            logger.info(f"Prepared data saved at  : {save_path}")

        except Exception as e:
            logger.error(f"Pipeline failed at data preparation \n {e}")
