"""
A importância do uso de interface se dá devido o problema da inversão de dependência,
onde um módolos de maior importância não deve ter dependência de módulos de níves de abstração menor
"""
from abc import ABC, abstractmethod
from uuid import UUID

from src.core.category.domain.category import Category


class CategoryRepository(ABC):
    @abstractmethod
    def save(self, category: Category) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id: UUID) -> Category | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: UUID) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, category: Category) -> None:
        raise NotImplementedError

    @abstractmethod
    def list_categories(self) -> list[Category]:
        raise NotImplementedError
    
    