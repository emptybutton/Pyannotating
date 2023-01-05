## Pyannotating
Allows you to create similar annotations without copying them all the time.<br>
It is advisable to place annotations created using this library in annotations.py file.

### Installation
`pip install pyannotating`

### Examples
Creating a factory of your annotations
```python
from pyannotating import CustomAnnotationFactory, input_annotation
from typing import Callable

handler_of = CustomAnnotationFactory(Callable, [[input_annotation], any])
```
Now you can create an annotation by this factory
```python
handler_of[int | float]
```

What is equivalent
```python
Callable[[int | float], any]
```

Also you can use Union with input_annotation
```python
summator_of = CustomAnnotationFactory(Callable, [[input_annotation | int, input_annotation], int])
summator_of[SomeCustomNumber]
```

What results in
```python
Callable[[SomeCustomNumber | int, SomeCustomNumber], int]
```

Ultimately you can annotate by the results of factories
```python
def some_operation_by(
    main: handler_of[int | float],
    *middleware: summator_of[SomeCustomNumber]
) -> handler_of[int | float]:
    ...
```
