# FileCatcher
a simple file searcher

---

This a module to search folder and file.

and can be used as:

    [PYTHON]
    import file_catcher

    searcher = file_catcher.FileCatcher('C:\\')
    searcher\
        .searchObjects('user', searcher.ObjectTypes.Folder, 0, searcher.SearchStrategy.StartWith, True)\
        .searchObjects('.exe', searcher.ObjectTypes.File, 3, searcher.SearchStrategy.EndWith)

    for item in searcher.lastSearchResult:
        print(item)