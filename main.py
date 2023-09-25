from quality_prediction_mlflow import logger
from quality_prediction_mlflow.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from quality_prediction_mlflow.pipeline.stage_02_data_validation import DataVaildationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} Completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try: 
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    data_validation = DataVaildationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
