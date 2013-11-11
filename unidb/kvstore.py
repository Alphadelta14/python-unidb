#!/usr/bin/env python
"""A key-value storage database."""

from basestore import BaseStore

class KVStore(BaseStore):
    def __init__(self):
        super(KVStore, self).__init__()
