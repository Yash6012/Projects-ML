import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            # for handeling file exception
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            artifact_dirs = [
                os.path.join(project_root, "artifacts"),
                os.path.join(project_root, "src", "components", "artifacts"),
            ]

            model_path = None
            preprocessor_path = None

            for artifact_dir in artifact_dirs:
                candidate_model_path = os.path.join(artifact_dir, "model.pkl")
                candidate_preprocessor_path = os.path.join(artifact_dir, "preprocessor.pkl")
                if os.path.exists(candidate_model_path) and os.path.exists(candidate_preprocessor_path):
                    model_path = candidate_model_path
                    preprocessor_path = candidate_preprocessor_path
                    break

            if model_path is None or preprocessor_path is None:
                raise FileNotFoundError("model.pkl or preprocessor.pkl not found in expected artifact directories")

            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

