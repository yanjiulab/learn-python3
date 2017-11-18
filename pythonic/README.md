Writing Great Python Code
=========================

Structuring Project
-------------------
### Structure of the Repository

### Structure of Package
- `__init__.py`  
- `sub-package/` (optional)
- `tests/`
    - `test_module.py`
- `module.py`
### Structure of Module
- module
    1. Indicating interpreter `#! /usr/bin/env python3`
    2. Indicating coding form `-*- coding: utf-8 -*-`
    3. Using comments started with `#` to show authors, copyrights, licence and so on. 
    4. Using `"""Explanation of this module"""` to explain your module
    5. Using `import` statement to import sth(modules or functions or anything else) and first built-in module then your owns.
    6. Writing your code
- test_module

Reading Great Code
------------------
- networkx
