# -*-coding:utf-8-*-

"""
This module contains a class `FileCatcher` to search file/folder.
"""

from enum import Enum

import os

class ObjectTypes(Enum):
    """
    Search target types.
    """
    File = 0
    Folder = 1

class SearchStrategy(Enum):
    """
    Search match strategy.
    """
    Strict = 0
    StartWith = 1
    EndWith = 2
    Contain = 3

class FileCatcher(object):
    """
    This is a file catcher.
    """

    __root_dir: str
    __last_search_result: list = []

    def __init__(self, root_dir: str):
        if not os.path.exists(root_dir):
            raise Exception('Given path does not exist')
        self.__root_dir = root_dir
        self.__last_search_result.append(root_dir)

    def __del__(self):
        __last_search_result = []
        __root_dir = ''

    def searchObjects(self,
                      obj_name: list,
                      obj_type: ObjectTypes,
                      depth: int = 0,
                      search_strategy: SearchStrategy = SearchStrategy.Strict,
                      ignore_case: bool = False):
        """
        searchObjects can search items as expect and store result in the `lastSearchResult`.
        
        paramters:
            obj_name : the string list given to match file/folder name.
            obj_type : decleare the item type.
            depth : how deep should search, if 0, file inn sub-folder will not be searced.
            search_strategy : how to match file name.
            ignore_case : should ignore item name case or not.
        
        return:
            This method will return this instance it-self.
            Thus can be used as:

                catcher\
                    .searchObjects(...)\
                    .searchObjects(...)\
                    .searchObjects(...)\
                    ...


        """
        fileList: list = []
        targetList: list
        if isinstance(obj_name, list):
            targetList = obj_name
        elif isinstance(obj_name, str):
            targetList = []
            targetList.append(obj_name)
        for target in targetList:
            self.__searchFileInList(target, fileList, obj_type, depth, search_strategy, ignore_case)
        self.__last_search_result = fileList
        return self

    def __getFileList(self, root, depth):
        if os.path.isfile(root):
            return [root]
        rst: list = []
        try:
            l = os.listdir(root)
        except Exception as ex:
            print('Error occurs when try get items in {0}:\n========\n{1}\n========\njump to next item... \n'
                  .format(root, ex))
            return []
        for item in l:
            item = os.path.join(root, item)
            item = os.path.abspath(item)
            rst.append(item)
            if os.path.isdir(item) and depth > 0 and os.access(item, os.F_OK) and os.access(item, os.R_OK):
                rst.extend(self.__getFileList(item, depth - 1))
        return rst

    def __searchFileInList(self, target, fileList, obj_type, depth, search_strategy, ignore_case):
        if not isinstance(target, str):
            raise Exception(
                'Given obj_name is not a list of string:\nGot {0}'.format(target))
        for item in self.__last_search_result:
            fullFileList = self.__getFileList(item, depth)
            for item2 in fullFileList:
                if obj_type is ObjectTypes.File and not os.path.isfile(item2):
                    continue
                elif obj_type is ObjectTypes.Folder and not os.path.isdir(item2):
                    continue
                if ignore_case:
                    item2 = item2.lower()
                    target = target.lower()
                if search_strategy is SearchStrategy.EndWith and not item2.endswith(target):
                    continue
                elif search_strategy is SearchStrategy.StartWith and not os.path.basename(item2).startswith(target):
                    continue
                elif search_strategy is SearchStrategy.Strict and not os.path.basename(item2) == target:
                    continue
                elif search_strategy is SearchStrategy.Contain and target not in os.path.basename(item2):
                    continue
                fileList.append(item2)

    @property
    def lastSearchResult(self):
        """
        All result will be saved here after each searching.
        """
        return self.__last_search_result

    def reset(self):
        """
        Clear all search result and set to root dir.
        """
        self.__last_search_result = self.__root_dir
