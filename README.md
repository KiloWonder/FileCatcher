# FileCatcher
a simple file searcher

---

This a module to search folder and file.

and can be used as:

    [PYTHON]
    from file_catcher import *

    searcher = FileCatcher('C:\\')
    searcher\
        .searchObjects('user', ObjectTypes.Folder, 0, SearchStrategy.StartWith, True)\
        .searchObjects('.exe', ObjectTypes.File, 3, SearchStrategy.EndWith)

    for item in searcher.lastSearchResult:
        print(item)

That will print all `.exe` files in the C:\user*\ with depth=3