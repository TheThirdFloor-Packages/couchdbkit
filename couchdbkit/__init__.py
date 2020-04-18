# -*- coding: utf-8 -
#
# This file is part of couchdbkit released under the MIT license.
# See the NOTICE for more information.

import logging

from .changes import ChangesStream
from .client import Database, Server, ViewResults
from .consumer import Consumer
from .designer import clone, document, push, pushapps, pushdocs
from .exceptions import BadValueError, BulkSaveError, DocsPathNotFound, DuplicatePropertyError, InvalidAttachment, \
    MultipleResultsFound, NoResultFound, PreconditionFailed, ReservedWordError, ResourceConflict, ResourceNotFound
from .external import External
from .loaders import BaseDocsLoader, FileSystemDocsLoader
from .resource import CouchdbResource, RequestFailed
from .schema import (AttachmentMixin, BooleanProperty, DateProperty, DateTimeProperty, DecimalProperty, DictProperty,
                     Document, DocumentBase, DocumentSchema, FloatProperty, IntegerProperty, ListProperty, Property,
                     QueryMixin, SchemaDictProperty, SchemaListProperty, SchemaProperty, SetProperty, StaticDocument,
                     StringDictProperty, StringListProperty, StringProperty, TimeProperty, contain, dict_to_json,
                     dict_to_json, dict_to_json, dict_to_python, value_to_python)
from .version import __version__, version_info

LOG_LEVELS = {
    "critical": logging.CRITICAL,
    "error":    logging.ERROR,
    "warning":  logging.WARNING,
    "info":     logging.INFO,
    "debug":    logging.DEBUG
}


def set_logging(level, handler=None):
    """
    Set level of logging, and choose where to display/save logs
    (file or standard output).
    """
    if not handler:
        handler = logging.StreamHandler()

    loglevel = LOG_LEVELS.get(level, logging.INFO)
    logger = logging.getLogger('couchdbkit')
    logger.setLevel(loglevel)
    format = r"%(asctime)s [%(process)d] [%(levelname)s] %(message)s"
    datefmt = r"%Y-%m-%d %H:%M:%S"

    handler.setFormatter(logging.Formatter(format, datefmt))
    logger.addHandler(handler)
