from abc import ABC, abstractmethod
from typing import List, Any


class DataStream(ABC):
    def  process_batch(self, data_batch: List[Any]) -> str:
        pass
    
