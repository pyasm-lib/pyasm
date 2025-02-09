from setuptools import setup, find_packages

setup(
    name="pyasm",
    version="0.4.0",
    author="PyASM Lib",
    description="A Python library which generates Assembly code.",
    long_description=open('README.md').read(),=
    long_description_content_type="text/markdown",
    url="https://github.com/pyasm-lib/pyasm",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
