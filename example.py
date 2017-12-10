import file_catcher

searcher = file_catcher.FileCatcher('C:\\')
searcher\
    .searchObjects(['user', 'programdata'], searcher.ObjectTypes.Folder, 0, searcher.SearchStrategy.StartWith, True)\
    .searchObjects('.exe', searcher.ObjectTypes.File, 2, searcher.SearchStrategy.EndWith)

for item in searcher.lastSearchResult:
    print(item)
