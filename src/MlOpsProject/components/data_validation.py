import pandas as pd
from src.MlOpsProject import logger
from src.MlOpsProject.config.configuration import DataValidationConfig




class DataValidation:

    def __init__(self,config:DataValidationConfig):
        self.config = config

    def validate_data(self, dataset :pd.DataFrame):

        column_info = {col: dataset[col].dtype for col in dataset.columns}
        schema = self.config.all_schema

        validation_status = True
        col_name_list =[]
        unmatched_datatype={}
        # # for checking only dataset columns name
        # for key,value in schema.items():
        #     if key not in dataset.columns.tolist():
        #         validation_status=False
        #         col_name_list.append(key)

        try:
            # for checking only dataset columns name and datatype
            for key, value in schema.items():

                if column_info.get(key) is None:
                    col_name_list.append(key)
                    validation_status = False
                elif column_info[key] != value:
                    unmatched_datatype[key]={'expected' : value, 'present':type(column_info[key])}
                    validation_status = False

            if  validation_status == False:
                if unmatched_datatype:
                    logger.error(f"validataion Failed due to data type mismatch: {unmatched_datatype}")
                else:
                    logger.error(f"validataion Failed : {col_name_list} not present in dataset")
            else:
                logger.error(f"validataion Successfull ")

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

        except Exception as e:
            logger.info(f"Error in Validating data:\n {e}")

