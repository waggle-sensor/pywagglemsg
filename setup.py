from setuptools import setup
from os import getenv

setup(
    name="wagglemsg",
    version=getenv("RELEASE_VERSION", "0.0.0"),
    description="Official Waggle Python message module",
    url="https://github.com/waggle-sensor/pywagglemsg",
    packages=[
        "wagglemsg",
    ],
    python_requires=">=3.6",
)
