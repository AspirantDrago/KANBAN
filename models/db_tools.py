from sqlalchemy import func
from sqlalchemy.ext.hybrid import Comparator


class DefaultComparator(Comparator):
    def __eq__(self, other):
        return func.coalesce(self.__clause_element__(), '') == other
