#!/usr/bin/env python3
"""This script annotate the fucntion below"""
from typing import Sequence, Any, Optional, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, Optional[None]]:
    """Annotate function"""
    if lst:
        return lst[o]
    else:
        return None
