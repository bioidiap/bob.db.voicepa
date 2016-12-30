#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Pavel Korshunov <pavel.korshunov@idiap.ch>
# Thu 6 Oct 21:43:22 2016

"""
The voicePA Database access methods for Bob

"""

from .query import Database
from .models import Client, File, Protocol, ProtocolFiles


def get_config():
    """
    Returns a string containing the configuration information.

    """
    import bob.extension
    return bob.extension.get_config(__name__)


# gets sphinx autodoc done right - don't remove it
def __appropriate__(*args):
  """Says object was actually declared here, an not on the import module.

  Parameters:

    *args: An iterable of objects to modify

  Resolves `Sphinx referencing issues
  <https://github.com/sphinx-doc/sphinx/issues/3048>`
  """
  for obj in args: obj.__module__ = __name__

__appropriate__(
    Database,
    Client,
    File,
    Protocol,
    ProtocolFiles,
    )


# gets sphinx autodoc done right - don't remove it
__all__ = [_ for _ in dir() if not _.startswith('_')]
