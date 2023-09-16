from dataclasses import dataclass
from pathlib import Path
from typing import Union, List
from src.MlOpsProject.constants.constant import CONFIG_PATH,SCHEMA_PATH,PARAMAS_PATH
from src.MlOpsProject.utils.common import read_yaml, create_directories

@dataclass(frozen=True)
class DataIngestionConfig:
    dataset_csv_file_path: Path
    database_name: str
    tabel_name: str
    extract_table_name : str




@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    dataset_path: Path
    all_schema: dict


@dataclass(frozen=True)
class DataPreparationConfig:
    root_dir : Path
    dataset_path : Path
    drop_column:Union[List[str], None]

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    normalization: bool
    normalization_column :List[str]
    normalize_scaler_path :Path
    data_split_ratio : tuple
    stratify : bool
    stratify_col : str



@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str




@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str




class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_PATH,
            params_filepath=PARAMAS_PATH,
            schema_filepath=SCHEMA_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            dataset_csv_file_path=config.dataset_csv_file_path,
            database_name=config.database_name,
            tabel_name=config.tabel_name,
            extract_table_name = config.extract_table_name
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            dataset_path=config.dataset_path,
            all_schema=schema,
        )

        return data_validation_config


    def get_data_preparation_config(self) -> DataPreparationConfig:

        config = self.config.data_preparation
        drop_column = self.schema.DROP_COLUMNS

        create_directories([config.root_dir])
        data_Prepration_config = DataPreparationConfig(
            root_dir=config.root_dir,
            dataset_path=config.dataset_path,
            drop_column = drop_column
        )

        return data_Prepration_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        data_transform_params = self.params.data_transform

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            normalization=data_transform_params.normalization,
            normalization_column = data_transform_params.normalization_column,
            data_split_ratio =data_transform_params.data_split_ratio,
            normalize_scaler_path = data_transform_params.normalize_scaler_path,
            stratify = data_transform_params.stratify,
            stratify_col =  data_transform_params.stratify_col
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.model_trainer.ElasticNet
        schema = self.schema

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.TARGET_COLUMN.name

        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.model_trainer.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            all_params=params,
            metric_file_name=config.metric_file_name,
            target_column=schema.name,
            mlflow_uri="https://dagshub.com/DeepLearnigProject/MLOps_demo.mlflow",

        )

        return model_evaluation_config