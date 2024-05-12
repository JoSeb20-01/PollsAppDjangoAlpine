import inspect
import importlib

from abc import abstractmethod, ABCMeta
from typing import Dict, Any, Optional

from django.conf import settings
from django.core.management.base import BaseCommand

class Seeder(metaclass=ABCMeta):
    """Class that seed data on database"""
    
    @abstractmethod
    def seed_data(self) -> Any:
        """Method that seed data on database"""


def get_seeders() -> Dict[str, Seeder]:
    """Get all declared seeders

    Returns:
        Dict[str, Seeder]: dictionary of seeder classes
    """

    seeders_dictionary = {}
    for app_name in settings.MY_APPS_WITH_SEEDERS:
        try:
            module = importlib.import_module(f'{app_name}.seeders')
            for name, seeder in inspect.getmembers(module, inspect.isclass):
                if issubclass(seeder, Seeder) and \
                    not seeder is Seeder:
                    seeders_dictionary[f"{app_name}.seeders.{name}"] = seeder
        except ModuleNotFoundError:
            pass
    
    return seeders_dictionary
        
def get_seeder_by_name(class_name: str) -> Optional[Seeder]:
    """Get specific seeder by class name

    Args:
        class_name (str) 

    Returns:
        Optional[Seeder]: Seeder class
    """
    for app_name in settings.MY_APPS_WITH_SEEDERS:
        try:
            module = importlib.import_module(f'{app_name}.seeders')
            for name, seeder in inspect.getmembers(module, inspect.isclass):
                if name == class_name:
                    return seeder
        except ModuleNotFoundError:
            pass
    
    return None
