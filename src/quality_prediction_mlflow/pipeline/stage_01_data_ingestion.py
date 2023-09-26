from quality_prediction_mlflow.config.configuration import ConfigurationManager
from quality_prediction_mlflow.components.data_ingestion import DataIngestion
from quality_prediction_mlflow import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file() # Download data 
        data_ingestion.extract_zip_files() # extract file 
    

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>stage {STAGE_NAME} Completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
