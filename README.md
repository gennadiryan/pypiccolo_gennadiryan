# pypiccolo

## Build

```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install build
python -m build
```

### Tear down build and build environment

```
deactivate
rm -rf dist src/pypiccolo_gennadiryan.egg-info env
```

## Setuptools

### Notes on package discovery, package data, and runtime configuration

- Setuptools offers a variety of means of discovering and/or specifying packages and modules to be included in the distribution (https://setuptools.pypa.io/en/latest/userguide/package_discovery.html). While setuptools offers means of implicitly discovering package layout (flat- vs. src-layout), and of explicitly specifying packages to be included, the means chosen by the present project is to explicitly specify package layout (i.e. using `package-dir` to specify src-layout), while not explicitly specifying packages to be included (i.e. not using `package`, in order to retain flexibility).

- Setuptools also offers several means of specifying data files to be included/excluded from the distribution (https://setuptools.pypa.io/en/latest/userguide/datafiles.html). Crucially, data files are meant to be read-only; it is recommended that shared and/or writable data files be installed outside the package directory in an appropriate location.

- Source distributions also include a number of files by default, including files matching `test[s]/test*.py`, license files (unless otherwise specified via `license-files`), `pyproject.toml`, files matching `setup.{cfg,py}`, README files, and `MANIFEST.in`, unless otherwise specified by `MANIFEST.in` (https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html); however, binary distributions do not. Crucially, binary distributions cannot depend on tests in `test[s]/test*.py`.

### Miscellaneous notes

- All of the `[project]` table entries of the `pyproject.toml` are standardized, with the exception of `license`. The PEP 639 standard defines new `[project]` table entries `license` (corresponding to a valid SPDX license expression) and `license-files` (corresponding to a list of license file glob paths). As `setuptools` is yet to support this standard, the legacy declaration is used instead; it is of the form `license = { text = "MIT License" }` or `license = { file = "LICENSE" }`. Note that other license files will still be included in the metadata, and hence both the source and binary distributions, unless the `license-files` entry of the `[tool.setuptools]` table is also used. It is expected that once `setuptools` adds support for PEP 639 that the `license-files` entry of the `[tools.setuptools]` table will be deprecated (or at least redundant).

- Inspect with `tar tf dist/*.tar.gz; unzip -l dist/*.whl;`

- Ensure backward-compatible with `setup.py` containing `from setuptools import setup; setup();`

## References

### Tutorials

- https://packaging.python.org/en/latest/tutorials/packaging-projects/

### Guides

- https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
- https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
- https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#platform-wheels
- https://packaging.python.org/en/latest/guides/packaging-binary-extensions/
- https://packaging.python.org/en/latest/guides/using-testpypi/
- https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
- https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html

### Specifications

- https://packaging.python.org/en/latest/specifications/pyproject-toml/
- https://packaging.python.org/en/latest/specifications/pypirc/
- https://pypi.org/classifiers/

### Examples

- https://github.com/pypa/sampleproject
