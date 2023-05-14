# -*- coding: utf-8 -*-
import datetime
import os.path
from typing import Dict


class Properties:

    def __init__(self):
        self.__properties__: Dict[str, str] = dict()

    def load(self, filename: str):
        if not os.path.exists(filename):
            raise IOError('file:%s not exists' % filename)
        with open(filename, mode='r', encoding='utf-8') as f:
            line = f.readline()
            while line:
                strip_line = line.strip()
                equal_symbol_index = strip_line.index('=')
                if equal_symbol_index > 0:
                    key = strip_line[0:equal_symbol_index]
                    value = strip_line[equal_symbol_index + 1:]
                    self.__properties__[key] = value
                line = f.readline()

    def get(self, key: str, default: str = None) -> str:
        return self.__properties__.get(key, default)

    def set(self, key: str, value: str):
        self.__properties__[key] = value

    def save(self, filename: str):
        with open(filename, mode='w', encoding='utf-8') as f:
            description = '# date:%s\n' % datetime.datetime.now()
            f.write(description)
            f.flush()
            for key in self.__properties__:
                line = '%s=%s\n' % (key, self.__properties__[key])
                f.write(line)
                f.flush()
