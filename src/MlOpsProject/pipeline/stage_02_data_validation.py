import pandas as pd
from src.MlOpsProject import logger
from src.MlOpsProject.components.data_validation import DataValidation
from src.MlOpsProject.config.configuration import ConfigurationManager

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:

    def __int__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validator = DataValidation(config = data_validation_config)
        dataset_path = data_validation_config.dataset_path
        dataset = pd.read_csv(dataset_path)

        #mimic the error
        # dataset =dataset.drop(['pH','quality'],axis=1)
        # dataset['volatile acidity'] =dataset['volatile acidity'].astype(str)
        # dataset['citric acid'] = dataset['citric acid'].astype(int)

        data_validator.validate_data(dataset)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e