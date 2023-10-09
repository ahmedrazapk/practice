from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in practice/__init__.py
from practice import __version__ as version

setup(
	name="practice",
	version=version,
	description="Practice app",
	author="ahmadrazapk",
	author_email="ahmad",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
