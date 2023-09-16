
from src.MlOpsProject import logger
from src.MlOpsProject.config.configuration import ConfigurationManager
from src.MlOpsProject.components.data_preparation import DataPreparation

STAGE_NAME = "Data Preparation stage"

class DataPreparationTrainingPipeline:
    def __init__(self):
        pass

    def prepared_dataset(self):
        config = ConfigurationManager()
        prepared_data_config = config.get_data_preparation_config()
        data_preparation = DataPreparation(config=prepared_data_config)
        data_preparation.dataset_drop_column()



if __name__ == '__main__':

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataPreparationTrainingPipeline()
        obj.prepared_dataset()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")
    except Exception as e:
        logger.exception(e)
        raise e