AIDSinfo Python API Wrapper
======================

A Python wrapper for the AIDSinfo drug information API.

AIDSinfo Documentation:  http://www.aidsinfo.nih.gov/Other/rss.aspx


Usage
-----

```python
>>> from aidsinfo import DrugInfo
>>> info = DrugInfo()
>>> info.search('abacavir')
{'abacavir': {'data': 'here'}}

>>> info.search('combivir')
{'combivir': {'data': 'here'}}
```


Copyright
---------

Copyright (c) 2011 Code for America Laboratories.

See LICENSE for details.
