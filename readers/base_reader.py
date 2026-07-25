from abc import ABC,abstractmethod
from models.order import Order

class BaseReader(ABC):

    @abstractmethod
    def read(self) -> list[Order]:
        """
        read data from any source and return list of order
        the design depends on how the reader reads the file
        in dict format or object then dataclass dttypes changes
        """
        pass