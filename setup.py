from setuptools import setup, find_packages

setup(
    name="strif",
    version="0.3",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "strif=strif.strif:main",
        ],
    },
)
