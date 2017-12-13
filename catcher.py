from enum import Enum


class ObjectTypes(Enum):
    File = 1
    Folder = 2
    Mix = 3


class MatchTypes(Enum):
    Strict = 0
    StartWith = 1
    EndWith = 2
    Contain = 3


def _search(area: list, item_type: ObjectTypes, depth: int):
    pass


class Item(object):
    pass


class Container(object):
    def __init__(self):
        self._searchResult = []

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

    @property
    def Result(self):
        return self._searchResult


class Searcher(object):
    _debug: bool

    def __init__(self,
                 is_debug: bool):
        self._debug = is_debug
        self._container = Container()

    def SearchIn(self,
                 area: list,
                 item_type: ObjectTypes = ObjectTypes.Mix,
                 depth: int = -1):
        """
        SearchIn creates a list to contains the file tree, and which will scan all the folders and files in (:param area).
        Then another list will be created to show the search result.
        :param area: a root folder that will be searched.
        :param item_type: type of item in the list of result.
        :param depth: an integer which point out how deep should searcher dig into root (:param area)
        :return: a result container type is Container.
        """
        pass

    @property
    def Result(self):
        return self._container.Result
