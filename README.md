# Life in Python
*Kyler Olsen*  
*Oct 2026*  
*SE 3250*  
*Project: Life in Python*

[Life in Python - Github](https://github.com/KylerAtSnow/life-python)
[Assignment - Canvas](https://snow.instructure.com/courses/1254077/assignments/19263999)

**Reflection**  
This was my first time using `uv`. I am undecided on if I like it yet, but I think I may possibly start using it all the time eventually. It does appear to be a very useful tool. I am excited for the Rust and Python project, it should be interesting. I have done C binding before, in atleast two different ways, I am interested to see how to do bindings with Rust.

Execution:
```
snow@moonkserver:~/f26/langs/hw/py-rs/life-python$ uv run pytest
=============================================================== test session starts ================================================================
platform linux -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/snow/f26/langs/hw/py-rs/life-python
configfile: pyproject.toml
collected 11 items

tests/cell_test.py ...........                                                                                                               [100%]

================================================================ 11 passed in 0.02s ================================================================
snow@moonkserver:~/f26/langs/hw/py-rs/life-python$ time uv run life-python
Cell(x=25001, y=-25000)
Cell(x=25000, y=-25000)
Cell(x=25002, y=-24999)
Cell(x=25001, y=-24998)
Cell(x=25002, y=-25000)

real    0m20.023s
user    0m20.002s
sys     0m0.021s
```

Commands:
```bash
cd f26/langs/hw/py-rs/life-python/
uv run pytest
time uv run life-python
```
