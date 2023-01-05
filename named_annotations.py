from abc import ABC, abstractmethod
from typing import Iterable, Mapping, Final


class AnnotationFactory(ABC):
    """
    Annotation factory class.
    Creates annotation by input other.

    Can be used via [] (preferred) or by normal call.
    """

    def __call__(self, annotation: any) -> any:
        return self._create_full_annotation_by(annotation)

    def __getitem__(self, annotation: any) -> any:
        return self._create_full_annotation_by(
            Union[annotation]
            if isinstance(annotation, Iterable)
            else annotation
        )

    @abstractmethod
    def _create_full_annotation_by(self, annotation: any) -> any:
        """Annotation Creation Method from an input annotation."""


class CustomAnnotationFactory(AnnotationFactory):
    """
    AnnotationFactory class delegating the construction of another factory's
    annotation.

    When called, replaces the 'annotation' strings from its arguments and their
    subcollections with the input annotation.
    """

    _input_annotation_annotation: str = '<input_annotation>'

    def __init__(self, original_factory: Mapping, annotations: Iterable):
        self._original_factory = original_factory
        self._annotations = tuple(annotations)

    @property
    def original_factory(self) -> Mapping:
        return self._original_factory

    @property
    def annotations(self) -> tuple:
        return self._annotations

    @classmethod
    @property
    def input_annotation_annotation(cls) -> str:
        return cls._input_annotation_annotation

    def __repr__(self) -> str:
        return "{factory}{arguments}".format(
            factory=(
                self._original_factory.__name__
                if hasattr(self._original_factory, '__name__')
                else self._original_factory
            ),
            arguments=str(self.__recursively_format(self._annotations)).replace('\'', str())
        )

    def _create_full_annotation_by(self, annotation: any) -> any:
        return self._original_factory[
            *self.__get_formatted_annotations_from(self._annotations, annotation)
        ]

    def __recursively_format(self, collection: Iterable) -> list:
        """
        Method for formatting the elements of a collection (and all of its
        sub-collections) as a list with possible element names or themselves.
        """

        formatted_collection = list()

        for item in collection:
            if isinstance(item, Iterable) and not isinstance(item, str):
                formatted_collection.append(self.__recursively_format(item))
            elif hasattr(item, '__name__'):
                formatted_collection.append(item.__name__)
            else:
                formatted_collection.append(item)

        return formatted_collection

