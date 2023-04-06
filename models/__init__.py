#!/usr/bin/python3
"""
It will allow us to define variables at a package level
This variables will be accessible by any module in the package
You can also import modules that you want to make available
to all packages
It allows someone to oraganize their code into logical units making
making it easier to re-use across projects
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

