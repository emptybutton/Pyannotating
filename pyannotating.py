from abc import ABC, abstractmethod
from typing import Optional, Any, Union, Iterable, Self, Mapping, Final, Callable, _UnionGenericAlias


class FormalAnnotation:
    """
    Class allowing to formally specify additional information about the input
    resource.

    When annotating, returns the input.

    Can be called via [] with some resource.
    """

    def __init__(self, instance_doc: Optional[str] = None):
        if instance_doc is not None:
            self.__doc__ = instance_doc

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"

    def __getitem__(self, resource: Any) -> Any:
        return resource


class AnnotationFactory(ABC):
    """
    Annotation factory class.
    Creates annotation by input other.

    Can be used via [] (preferred) or by normal call.
    """

    def __call__(self, annotation: Any) -> Any:
        return self._create_full_annotation_by(annotation)

    def __getitem__(self, annotation: Any) -> Any:
        return self._create_full_annotation_by(
            Union[annotation]
            if isinstance(annotation, Iterable)
            else annotation
        )

    @abstractmethod
    def _create_full_annotation_by(self, annotation: Any) -> Any:
        """Annotation Creation Method from an input annotation."""


class InputAnnotationAnnotation:
    """
    Singleton class for the annotation of the conditional empty space, in which
    the input type in the CustomAnnotationFactory should be placed.

    Supports | to create Union type.
    """

    _instance: Optional[Self] = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance') or cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

    def __repr__(self) -> str:
        return '<input_annotation>'

    def __or__(self, other: Any) -> Union:
        return Union[self, other]

    def __ror__(self, other: Any) -> Union:
        return Union[other, self]


class AnnotationTemplate(AnnotationFactory):
    """
    AnnotationFactory class delegating the construction of another factory's
    annotation.

    When called, replaces the InputAnnotationAnnotation instances from its
    arguments and their subcollections with the input annotation.
    """

    def __init__(self, original_factory: Mapping, annotations: Iterable):
        self._original_factory = original_factory
        self._annotations = tuple(annotations)

    @property
    def original_factory(self) -> Mapping:
        return self._original_factory

    @property
    def annotations(self) -> tuple:
        return self._annotations

    def __repr__(self) -> str:
        return "{factory}{arguments}".format(
            factory=(
                self._original_factory.__name__
                if hasattr(self._original_factory, '__name__')
                else self._original_factory
            ),
            arguments=str(self.__recursively_format(self._annotations)).replace('\'', str())
        )

    def _create_full_annotation_by(self, annotation: Any) -> Any:
        return self._original_factory[
            *self.__get_formatted_annotations_from(self._annotations, annotation)
        ]

    def __get_formatted_annotations_from(self, annotations: Iterable, replacement_annotation: Any) -> tuple:
        """
        Recursive function to replace element(s) of the input collection (and
        its subcollections) equal to the annotation anonation with the input
        annotation.
        """

        formatted_annotations = list()

        for annotation in annotations:
            if isinstance(annotation, InputAnnotationAnnotation):
                annotation = replacement_annotation

            elif isinstance(annotation, Iterable) and not isinstance(annotation, str):
                annotation = self.__get_formatted_annotations_from(
                    annotation,
                    replacement_annotation
                )

            elif type(annotation) in (Union, _UnionGenericAlias, type(int | float)):
                annotation = Union[
                    *self.__get_formatted_annotations_from(
                        annotation.__args__,
                        replacement_annotation
                    )
                ]

            formatted_annotations.append(annotation)

        return tuple(formatted_annotations)

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


# Pre-created instance without permanent formal creation of a new one.
input_annotation: Final[InputAnnotationAnnotation] = InputAnnotationAnnotation()

number: Final = int | float | complex