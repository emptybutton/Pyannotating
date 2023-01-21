from typing import Any, Union, Optional, Callable, Iterable, Sized

from pytest import mark

from pyannotating import FormalAnnotation, InputAnnotationAnnotation, AnnotationTemplate, input_annotation, Special


@mark.parametrize(
    "input_resource, result",
    [(42, 42), (Any, Any), (int | float, int | float)]
)
def test_formal_annotation(input_resource: Any, result: Any):
    assert FormalAnnotation()[input_resource] == result


@mark.parametrize(
    'doc',
    ["Documentation", "\n\t.!#@$2*-_\n", b"\tHello\n\tWorld\n\t!", str()]
)
def test_formal_annotation_documenting(doc: str):
    assert FormalAnnotation(doc).__doc__ == doc
