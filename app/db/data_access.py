from abc import ABC, abstractmethod
from typing import Dict, Optional, List


class DBInterface(ABC):
    """General interface for data store operations."""

    @abstractmethod
    def create(self, item_data: Dict) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def get(self, item_id: int) -> Optional[Dict]:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Dict]:
        raise NotImplementedError

    @abstractmethod
    def update(self, item_id: int, update_data: Dict) -> Optional[Dict]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id: int) -> bool:
        raise NotImplementedError
