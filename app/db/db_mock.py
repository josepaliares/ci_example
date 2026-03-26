import threading
from typing import Dict, Optional, List
from app.db.data_access import DBInterface


class MockDB(DBInterface):
    """In-memory generic mock database for items keyed by int id."""

    def __init__(self):
        self._lock = threading.Lock()
        self._items: Dict[int, Dict] = {}
        self._next_id = 1

    def create(self, item_data: Dict) -> Dict:
        if not isinstance(item_data, dict):
            raise ValueError("item_data must be a dict")

        with self._lock:
            item_id = self._next_id
            self._next_id += 1
            record = {**item_data, "id": item_id}
            self._items[item_id] = record
            return record

    def get(self, item_id: int) -> Optional[Dict]:
        return self._items.get(item_id)

    def list(self) -> List[Dict]:
        return list(self._items.values())

    def update(self, item_id: int, update_data: Dict) -> Optional[Dict]:
        with self._lock:
            existing = self._items.get(item_id)
            if existing is None:
                return None
            updated = {**existing, **update_data, "id": item_id}
            self._items[item_id] = updated
            return updated

    def delete(self, item_id: int) -> bool:
        with self._lock:
            return self._items.pop(item_id, None) is not None
