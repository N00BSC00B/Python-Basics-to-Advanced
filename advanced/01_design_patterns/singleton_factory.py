"""
Title: Singleton and Factory Design Pattern Example
Author: Python Design Patterns Contributors
Description:
    Demonstrates the Singleton and Factory Method design patterns in Python
    with a Logger and Animal creation system.
Date: October 2025
"""

from threading import Lock
from typing import Type, Dict


# =============================================================================
# 1. SINGLETON PATTERN (Thread-safe)
# =============================================================================
class SingletonMeta(type):
    """A thread-safe implementation of Singleton."""
    _instance = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Logger(metaclass=SingletonMeta):
    """A simple logger class using Singleton pattern."""
    def log(self, msg: str) -> None:
        print(f"[LOG]: {msg}")


# =============================================================================
# 2. FACTORY PATTERN
# =============================================================================
class Animal:
    """Base Animal class."""
    def speak(self) -> str:
        raise NotImplementedError("Subclasses must implement 'speak' method.")


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"


class AnimalFactory:
    """Factory for creating Animal instances dynamically."""
    _registry: Dict[str, Type[Animal]] = {}

    @classmethod
    def register_animal(cls, name: str, animal_cls: Type[Animal]) -> None:
        cls._registry[name.lower()] = animal_cls

    @classmethod
    def create(cls, name: str) -> Animal:
        if name.lower() not in cls._registry:
            raise ValueError(f"Unknown animal type: {name}")
        return cls._registry[name.lower()]()


# Register animals dynamically
AnimalFactory.register_animal("dog", Dog)
AnimalFactory.register_animal("cat", Cat)


# =============================================================================
# 3. DEMONSTRATION
# =============================================================================
if __name__ == "__main__":
    logger = Logger()
    logger.log("Application started.")

    pet_type = "dog"
    pet = AnimalFactory.create(pet_type)
    logger.log(f"Created a {pet_type} that says: {pet.speak()}")

    # Validate Singleton behavior
    logger2 = Logger()
    assert logger is logger2
    logger.log("Verified Singleton: Both logger instances are identical.")

    logger.log("Application finished successfully.")
