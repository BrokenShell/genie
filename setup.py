from setuptools import setup, Extension
from Cython.Build import cythonize
from platform import system


compiler_args = {
    "Darwin": ["-std=gnu++20", "-Ofast"],
    "Linux": ["-std=gnu++17", "-O3"],
    "Windows": ["/std:c++20", "/O2"],
}.get(system())

setup(
    name="Genie",
    ext_modules=cythonize(
        Extension(
            name="Genie",
            sources=["Genie.pyx"],
            language=["c++"],
            extra_compile_args=compiler_args,
        ),
        compiler_directives={
            "embedsignature": True,
            "language_level": 3,
        },
    ),
    author="Robert Sharp",
    author_email="webmaster@sharpdesigndigital.com",
    version="0.0.1",
    description="High Performance Random Value Toolkit",
)
