"""
Provides functunality for making predictions.

Contains ModelInferenceService class, which offers methods to
load a model from a file, and make predictions using the loaded model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings


class ModelInferenceService:
    """
    A service class for making predictions.

    This class frovides functunalities to load a model from a specified
    path, and make predictions using the loaded model.

    Attributes:
        model: ML model menaged by this service. Initially set to None.
        model_path: Directory to save the model to.
        model_name: Name of the saved model.

    Methods:
        __init__: constructor that initialize inference service.
        load_model: Load model from file / build it if it doesnt exist.
        predict: makes a prediction using loaded model.
    """

    def __init__(self) -> None:
        """Initialize the ModelInferenceService."""
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def load_model(self) -> None:
        """
        Load model from a specific path & build a model if doesnt exist.

        Raises:
            FileNotFoundError: when model file not exist at the specified dir
        """
        logger.info(
            f'checking for model existance in:'
            f' {self.model_path}/{self.model_name}',
        )

        model_path = Path(
            f'{self.model_path}/{self.model_name}',
        )

        if not model_path.exists():
            raise FileNotFoundError('Model does not exist')

        logger.info(
            f'model {self.model_name} found -->'
            f'loading model configuration file',
        )

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)

    def predict(self, input_parameters: list) -> list:
        """
        Make a prediction using loaded model.

        Takes input parameters and passes it to the
        model loaded using pickle file.

        Args:
            input_parameters (list): Input data for making prediction.

        Returns:
            list: The predition result from this model.
        """
        logger.info('making prediction')

        return self.model.predict([input_parameters])
