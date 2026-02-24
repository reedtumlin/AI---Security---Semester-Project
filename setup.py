from setuptools import setup, Extension
from Cython.Build import cythonize   # <-- add this import
import numpy as np
import sys

extra_compile_args = []
if sys.platform == "win32":
    extra_compile_args.append("/std:c11")   # optional, you can omit
else:
    extra_compile_args += ["-Wno-cpp", "-Wno-unused-function", "-std=c99"]

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
        include_dirs=[np.get_include(), '../common'],
        extra_compile_args=extra_compile_args,
    )
]

setup(
    name='pycocotools',
    packages=['pycocotools'],
    package_dir={'pycocotools': 'pycocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='2.0',
    ext_modules=cythonize(ext_modules, compiler_directives={'language_level': '3'}),
)