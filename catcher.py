from enum import Enum


class ObjectTypes(Enum):
    File = 0
    Folder = 1


class MatchTypes(Enum):
    Strict = 0
    StartWith = 1
    EndWith = 2
    Contain = 3


class Item(object):
    pass


class Searcher(object):
    _debug: bool
    _searchResult: list

    def __init__(self,
                 is_debug: bool):
        self._debug = is_debug

    def SearchIn(self,
                 area: list,
                 item_type: ObjectTypes,
                 depth: int = -1):
        pass

    def And(self,
            condition: list,
            item_type: ObjectTypes,
            depth: int,
            match_strategy: MatchTypes = MatchTypes.Contain,
            ignore_case: bool = False):
        pass

    def Or(self,
           condition: list,
           item_type: ObjectTypes,
           depth: int,
           match_strategy: MatchTypes = MatchTypes.Contain,
           ignore_case: bool = False):
        pass

    def Xor(self,
            condition: list,
            item_type: ObjectTypes,
            depth: int,
            match_strategy: MatchTypes = MatchTypes.Contain,
            ignore_case: bool = False):
        pass

    def AndNot(self,
               condition: list,
               item_type: ObjectTypes,
               depth: int,
               match_strategy: MatchTypes = MatchTypes.Contain,
               ignore_case: bool = False):
        pass

    def OrNot(self,
              condition: list,
              item_type: ObjectTypes,
              depth: int,
              match_strategy: MatchTypes = MatchTypes.Contain,
              ignore_case: bool = False):
        pass

    def XorNot(self,
               condition: list,
               item_type: ObjectTypes,
               depth: int,
               match_strategy: MatchTypes = MatchTypes.Contain,
               ignore_case: bool = False):
        pass

    @@property
    def Result(self):
        return self._searchResult

