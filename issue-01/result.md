Запускаю
```
python -m doctest -v -o NORMALIZE_WHITESPACE -o ELLIPSIS morse.py
```

Результат:
```
Trying:
    decode('... --- ...')
Expecting:
    'SOS'
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('AAAAA') #doctest: +ELLIPSIS
Expecting:
    '.-....-'
ok
1 items had no tests:
    morse
2 items passed all tests:
   1 tests in morse.decode
   2 tests in morse.encode
3 tests in 3 items.
3 passed and 0 failed.
Test passed.
```
