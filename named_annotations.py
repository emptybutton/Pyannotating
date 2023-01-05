from abc import ABC, abstractmethod


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


