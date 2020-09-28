python3

```
 make init
 make test
 ```


example output:

```
➜  pyre-test git:(master) ✗ make init
python3 -m venv ./venv
./venv/bin/pip install --upgrade pip
Collecting pip
  Using cached pip-20.2.3-py2.py3-none-any.whl (1.5 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.1.1
    Uninstalling pip-20.1.1:
      Successfully uninstalled pip-20.1.1
Successfully installed pip-20.2.3
./venv/bin/pip install -r requirements.txt
Collecting pyre-check
  Using cached pyre_check-0.0.56-py3-none-macosx_10_11_x86_64.whl (16.1 MB)
Processing /Users/ilx/Library/Caches/pip/wheels/ae/f3/c6/ffd1b0df0828cf685b0c863655f166b426cf1a3f62578206f1/pywatchman-1.4.1-cp38-cp38-macosx_10_15_x86_64.whl
Collecting libcst>=0.3.6
  Using cached libcst-0.3.11-py3-none-any.whl (501 kB)
Collecting pyre-extensions
  Using cached pyre_extensions-0.0.18-py3-none-any.whl (8.3 kB)
Collecting dataclasses
  Using cached dataclasses-0.6-py3-none-any.whl (14 kB)
Processing /Users/ilx/Library/Caches/pip/wheels/91/cf/b0/0c9998060b55ca80ea7a50a8639c3bdc6ba886eeff014bc9ac/psutil-5.7.2-cp38-cp38-macosx_10_15_x86_64.whl
Processing /Users/ilx/Library/Caches/pip/wheels/13/90/db/290ab3a34f2ef0b5a0f89235dc2d40fea83e77de84ed2dc05c/PyYAML-5.3.1-cp38-cp38-macosx_10_15_x86_64.whl
Collecting typing-extensions>=3.7.4.2
  Using cached typing_extensions-3.7.4.3-py3-none-any.whl (22 kB)
Collecting typing-inspect>=0.4.0
  Using cached typing_inspect-0.6.0-py3-none-any.whl (8.1 kB)
Collecting mypy-extensions>=0.3.0
  Using cached mypy_extensions-0.4.3-py2.py3-none-any.whl (4.5 kB)
Installing collected packages: pywatchman, pyyaml, typing-extensions, mypy-extensions, typing-inspect, libcst, pyre-extensions, dataclasses, psutil, pyre-check
Successfully installed dataclasses-0.6 libcst-0.3.11 mypy-extensions-0.4.3 psutil-5.7.2 pyre-check-0.0.56 pyre-extensions-0.0.18 pywatchman-1.4.1 pyyaml-5.3.1 typing-extensions-3.7.4.3 typing-inspect-0.6.0
➜  pyre-test git:(master) ✗ make test
./venv/bin/pyre check
 ƛ Found 2 type errors!
test.py:4:12 Undefined or invalid type [11]: Annotation `t.Amount` is not defined as a type.
test.py:5:11 Unbound name [10]: Name `Amount` is used but not defined in the current scope.
make: *** [test] Error 1

```
