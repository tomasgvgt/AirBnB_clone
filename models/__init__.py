#!/usr/bin/python3
"""
ahorita
"""
from models.engine.file_storage import FileStorage

"""
create a instance of FileStorage so
FileStorage can be use in other classes
"""
storage = FileStorage()
storage.reload()  # reload all the object previously created
