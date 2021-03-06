# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import lib, get_string, get_string_array
from ._utils import codec


def ActiveClassName():
    """(read-only) Returns name of active class."""
    return get_string(lib.ActiveClass_Get_ActiveClassName())


def AllNames():
    """(read-only) Array of strings consisting of all element names in the active class."""
    return get_string_array(lib.ActiveClass_Get_AllNames)


def Count():
    """(read-only) Number of elements in Active Class. Same as NumElements Property."""
    return lib.ActiveClass_Get_Count()


def First():
    """(read-only) Sets first element in the active class to be the active DSS object. If object is a CktElement, ActiveCktELment also points to this element. Returns 0 if none."""
    return lib.ActiveClass_Get_First()


def Name(*args):
    """Name of the Active Element of the Active Class"""
    # Getter
    if len(args) == 0:
        return get_string(lib.ActiveClass_Get_Name())

    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.ActiveClass_Set_Name(Value)


def Next():
    """(read-only) Sets next element in active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element.  Returns 0 if no more."""
    return lib.ActiveClass_Get_Next()


def NumElements():
    """(read-only) Number of elements in this class. Same as Count property."""
    return lib.ActiveClass_Get_NumElements()


_columns = ["ActiveClassName", "Name", "NumElements"]
__all__ = [
    "ActiveClassName",
    "AllNames",
    "Count",
    "First",
    "Name",
    "Next",
    "NumElements",
]
