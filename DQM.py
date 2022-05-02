from logger import logging

class schema_check:
    def __init__(self,schema_file_path):
        self.schema_file_path = schema_file_path
        self.log = logging()

    def config_check(self):
        
