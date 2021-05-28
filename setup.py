from setuptools import setup

REQUIREMENTS = []
with open("requirements.txt", "r") as f:
    REQUIREMENTS = f.read().splitlines()

README = ""
with open("readme.md", "r") as f:
    README = f.read()

setup(
    name="idevision.py",
    author="isaa_ctaylor",
    license="GPL-3.0 License",
    packages="idevision",
    description="A python wrapper for the idevision api",
    long_description=README,
    install_requires=REQUIREMENTS
)