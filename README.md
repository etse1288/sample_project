

TODOs
- [ ] build wheel files in `build` 
  - https://stackoverflow.com/a/74659682
  - `python -m build` vs `pip wheel .`
  - `pip wheel --no-deps -w dist .`
- [ ] tox for multiple python versions
- [ ] pylint with pytest
- [ ] mypy with pytest
- [ ] project settings to control pylint and mypy
- [ ] make or Cmake with clean
  - allow use of pyc_wheel (`python -m pyc_wheel`) to release `.pyc` files only
- [ ] find a shell on Windows
- [ ] Look into different backend build systems
- [ ] Only include files i specify (manifest?)


BKMs
- List wheel files: `python -m zipfile --list path/to/my-wheel-file.whl`
- 