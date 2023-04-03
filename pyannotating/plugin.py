from typing import Optional, Callable, Type, Mapping, TypeVar

from mypy.plugin import Plugin, DynamicClassDefContext


class PyannotatingPlugin(Plugin):


def plugin(version: str) -> Type[PyannotatingPlugin]:
    return PyannotatingPlugin