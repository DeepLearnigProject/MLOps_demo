import pandas as pd
import os
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from src.MlOpsProject import logger
from src.MlOpsProject.config.configuration import DataTransformationConfig
from src.MlOpsProject.utils.common import save_data_in_pickle
class DataTransform:
    def __init__(self, config:DataTransformationConfig):
        self.config = config

    def tranform_and_save_data(self):
        try:
            data_path = self.config.data_path
            df = pd.read_csv(data_path)
            df = self.nomalize_data(df)
            train_df,test_df = self.split_data_into_train_test(df)

            train_df_path = Path(os.path.join(self.config.normalize_scaler_path,'train_df.csv'))
            test_df_path =  Path(os.path.join(self.config.normalize_scaler_path,'test_df.csv'))
            train_df.to_csv(train_df_path,index=False)
            logger.info(f"train data is saved at  : {train_df_path}")
            test_df.to_csv(test_df_path,index=False)
            logger.info(f"test data is saved at  : {test_df_path}")

        except Exception as e:
            logger.error(f"Error in data transform and save data: \n {e}")

    def nomalize_data(self,df:pd.DataFrame):
        try:
            if self.config.normalization:
                norm_col = self.config.normalization_column
                scaler = StandardScaler()
                df[norm_col] = scaler.fit_transform(df[norm_col])
                logger.info("Scaler is done")
                scaler_save_path  = Path(os.path.join(self.config.normalize_scaler_path,'StandardScaler.pcl'))
                save_data_in_pickle(data=scaler,path=scaler_save_path)
                # logger.info(f"Scaler is saved at : {scaler_save_path}")
            return df
        except Exception as e:
            logger.error(f"Error in Normalization: \n {e}")

    def split_data_into_train_test(self,df:pd.DataFrame):
        try:
            test_ratio = self.config.data_split_ratio[1]
            # train_ratio = self.config.data_split_ratio[0]
            if self.config.stratify:

                train_df,test_df = train_test_split(df, test_size=test_ratio, random_state=42,
                                                    stratify=df[self.config.stratify_col])
            else:
                train_df, test_df = train_test_split(df, test_size=test_ratio, random_state=45)
            logger.info(f"train data shape : {train_df.shape},test data shape : {test_df.shape}")
            return train_df, test_df
        except Exception as e:
            logger.error(f"Error in Data splliting \n {e}")




