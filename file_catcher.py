# -*-coding:utf-8-*-

"""
This module contains a class `FileCatcher` to search file/folder.
"""

from enum import Enum

import os


class FileCatcher(object):
    """
    This is a file catcher.
    """

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
        pass

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
        targetList: list = []
        if isinstance(obj_name, list):
            targetList = obj_name
        elif isinstance(obj_name, str):
            targetList.append(obj_name)
        for target in targetList:
            self.__searchFileInList(target, fileList, obj_type, depth, search_strategy, ignore_case)
        self.__last_search_result = fileList
        return self

    def __getFileList(self, root, depth):
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
            raise Exception('Given obj_name is not a list of string:\nGot {0}'.format(target))
        for item in self.__last_search_result:
            fullFileList = self.__getFileList(item, depth)
            for item in fullFileList:
                if obj_type is self.ObjectTypes.File and not os.path.isfile(item):
                    continue
                elif obj_type is self.ObjectTypes.Folder and not os.path.isdir(item):
                    continue
                if ignore_case:
                    item = item.lower()
                    target = target.lower()
                if search_strategy is self.SearchStrategy.EndWith and not item.endswith(target):
                    continue
                elif search_strategy is self.SearchStrategy.StartWith and not os.path.basename(item).startswith(target):
                    continue
                elif search_strategy is self.SearchStrategy.Strict and not os.path.basename(item) == target:
                    continue
                elif search_strategy is self.SearchStrategy.Contain and target not in os.path.basename(item):
                    continue
                fileList.append(item)
    
    @property
    def lastSearchResult(self):
        return self.__last_search_result

    def reset(self, value):
        self.__last_search_result = self.__root_dir


def handleFile(item: str):
    if os.access(item, os.F_OK) and os.access(item, os.R_OK) and os.access(item, os.W_OK):
        file = open(item, 'r+')
        try:
            lines = file.readlines()
            keyLine: int = -1
            valueLine: int = -1
            for index in range(len(lines)):
                # for line in lines:
                line = lines[index]
                if line.startswith('[http]'):
                    keyLine = index
                elif line.endswith('proxy = 127.0.0.1:50255') and keyLine >= 0:
                    valueLine = index
                    break
            if keyLine == -1:
                file.writelines(
                    ['\n[http]', '\n    proxy = 127.0.0.1:50255'])
                print('{0} has been changed'.format(item))
            elif valueLine == -1:
                file.close()
                file = open(item, 'w')
                lines.insert(keyLine + 1, '    proxy = 127.0.0.1:50255\n')
                file.writelines(lines)
                print('{0} has been changed'.format(item))
        except Exception as ex:
            print(
                'Error occurs when try to read and write file `{0}`:\n\r{1}'.format(item, ex))
        finally:
            file.close()
