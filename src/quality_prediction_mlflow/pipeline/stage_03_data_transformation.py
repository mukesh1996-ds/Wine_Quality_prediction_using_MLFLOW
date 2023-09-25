from quality_prediction_mlflow.config.configuration import ConfigurationManager
from quality_prediction_mlflow.components.data_transformation import DataTransformation
from quality_prediction_mlflow import logger
from pathlib import Path


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts\data_validation\status.txt"),"r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("You data scheme is not valid")

        except Exception as e:
            print(e) 

if __name__ == "__main__":
    try:
        logger.info(f"transformation pipeline {STAGE_NAME} started")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"transformation pipeline {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e
        