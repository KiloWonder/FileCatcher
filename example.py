from file_catcher import *

searcher = FileCatcher('C:\\')
searcher\
    .searchObjects(['user', 'progr'], ObjectTypes.Folder, 0, SearchStrategy.StartWith, True)\
    .searchObjects('.exe', ObjectTypes.File, 2, SearchStrategy.EndWith)

for item in searcher.lastSearchResult:
    print(item)
