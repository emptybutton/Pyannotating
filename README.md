## Pyannotating
Allows you to structure your annotations and put more information into them.<br>
Templates created with this library should preferably be placed in the annotations.py file.

### Installation
`pip install pyannotating`

### Features
You can create a template of your annotations
```python
from pyannotating import *
from typing import Callable, Any, Optional, Iterable

handler_of = AnnotationTemplate(Callable, [[input_annotation], Any])
```
and then create an annotation by this template
```python
handler_of[int | float]
```

what is equivalent
```python
Callable[[int | float], Any]
```

Also you can nest templates inside each other
```python
optional_handler_of = AnnotationTemplate(
    Callable,
    [[input_annotation], AnnotationTemplate(Optional, [input_annotation])]
)

optional_handler_of[int]
```

what results in
```python
Callable[[int], Optional[int]]
```

and use input_annotation in conjunction with something else
```python
summator_of = AnnotationTemplate(Callable, [[input_annotation | int, input_annotation], int])
summator_of[float]
```

to get
```python
Callable[[float | int, float], int]
```

In addition, you can integrate comments with your annotations
```python
even = FormalAnnotation("Formal annotation of even numbers.")

number: even[int | float] = 42
```

or annotate downcasts
```python
def transform(collection: Special[range, Iterable]) -> Any:
    ...
```

or just use some pre-made templates
```python
many_or_one[Callable]
method_of[int]
```

for getting
```python
Callable | Iterable[Callable]
Callable[[int, ...], Any]
```