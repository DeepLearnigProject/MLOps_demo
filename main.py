from src.MlOpsProject import logger
from src.MlOpsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.MlOpsProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.MlOpsProject.pipeline.stage_03_data_preparation import DataPreparationTrainingPipeline
from src.MlOpsProject.pipeline.stage_04_data_transform import DataTransformTrainingPipeline
from src.MlOpsProject.pipeline.stage_05_model_trainer import ModelTrainerTrainingPipeline

# STAGE_NAME = "Data Ingestion stage"
# try:
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#    data_ingestion = DataIngestionTrainingPipeline()
#    data_ingestion.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")
# except Exception as e:
#         logger.exception(e)
#         raise e

#
# STAGE_NAME = "Data Validation stage"
#
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = DataValidationTrainingPipeline()
#     obj.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = "Data Preparation stage"
#
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = DataPreparationTrainingPipeline()
#     obj.prepared_dataset()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")
# except Exception as e:
#     logger.exception(e)
#     raise e
#
# STAGE_NAME = "Data Transform stage"
#
# if __name__ =='__main__':
#     try:
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = DataTransformTrainingPipeline()
#         obj.transform_data()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x\n")
#     except Exception as e:
#         logger.exception(e)
#         raise e


STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
