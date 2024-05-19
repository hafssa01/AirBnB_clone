#!/usr/bin/python3
"""
This is __init__ module
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()