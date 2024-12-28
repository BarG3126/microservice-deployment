"""
Provides functunality for building ML model.

Contains ModelBuilderService class, that offers methods to
train a model, and save it to a specified directory.
"""


from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelBuilderService:
    """
    A service class for building and saving ML model.

    This class frovides functunalities to train a model and save
    it to specified path.

    Attributes:
        model_path: Directory to save the model to.
        model_name: Name of the saved model.

    Methods:
        __init__: constructor that initialize ModelBuilderService.
        train_model: Train model and saves it to a specified directory.
    """

    def __init__(self) -> None:
        """Initialize the ModelBuildService."""
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def train_model(self) -> None:
        """Train model from a specific path & save to model's dir."""
        logger.info(
            f'building model config file at:'
            f' {self.model_path}/{self.model_name}',
        )
        build_model()
