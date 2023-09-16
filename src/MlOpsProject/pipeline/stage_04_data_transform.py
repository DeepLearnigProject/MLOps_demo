from src.MlOpsProject import logger
from src.MlOpsProject.components.data_transform import DataTransform
from src.MlOpsProject.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transform stage"

class DataTransformTrainingPipeline:
    def __init__(self):
        pass

    def transform_data(self):
        config = ConfigurationManager()
        data_transfom_config = config.get_data_transformation_config()
        data_transfom = DataTransform(config=data_transfom_config)
        data_transfom.tranform_and_save_data()

if __name__ =='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformTrainingPipeline()
        obj.transform_data()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")
    except Exception as e:
        logger.exception(e)
        raise e