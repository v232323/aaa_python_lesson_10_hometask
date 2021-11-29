#issue-01
Запустить можно из IDE. Для этого сделаны: 
```python
import doctest
```

```python
doctest.testmod()
```

Для запуска из командной строки:
```
python -m doctest -v -o NORMALIZE_WHITESPACE -o ELLIPSIS morse.py
```
