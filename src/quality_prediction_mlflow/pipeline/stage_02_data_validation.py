from quality_prediction_mlflow.config.configuration import ConfigurationManager
from quality_prediction_mlflow.components.data_validation import DataValiadtion
from quality_prediction_mlflow import logger

STAGE_NAME = "Data Validation Stage"

class DataVaildationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()



if __name__ == "__main__":
    try: 
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        obj = DataVaildationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e