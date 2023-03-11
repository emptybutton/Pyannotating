## Pyannotating
Structures your annotations and puts more information into them.

### Installation
`pip install pyannotating`

### Examples
Create annotation templates
```python
from typing import Callable, Any, Optional, Iterable

from pyannotating import *


handler_of = AnnotationTemplate(Callable, [[input_annotation], Any])
handler_of[int | float]
```
```python
Callable[[int | float], Any]
```

in a nested way
```python
optional_reformer_of = AnnotationTemplate(
    Callable,
    [[input_annotation], AnnotationTemplate(Optional, [input_annotation])]
)

optional_reformer_of[int]
```
```python
Callable[[int], Optional[int]]
```

with non-strict input annotation
```python
summator_of = AnnotationTemplate(Callable, [[input_annotation | int, input_annotation], int])
summator_of[float]
```
```python
Callable[[float | int, float], int]
```

Integrate comments into annotations
```python
even = FormalAnnotation("Formal annotation of even numbers.")

number: even[int | float] = 42
```

or subgroups of existing types
```python
natural_numbers = Subgroup(int, lambda number: number > 0)

isinstance(14, natural_numbers)
isinstance(-1.2, natural_numbers)

64 in natural_numbers
```
```python
True
False
True
```

or downcasts
```python
def transform(numbers: Special[range, Iterable[int]], additional: Special[None] = None) -> Any:
    ...

# Equals to

def transform(numbers: Iterable[int], additional: Any = None) -> Any:
    ...
```


or just some pre-made templates and annotations
```python
many_or_one[int | float]
number
```
```python
int | float | Iterable[int | float]
int | float | complex
```