from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in todo/__init__.py
from todo import __version__ as version

setup(
	name="todo",
	version=version,
	description="This is a to-do list app.",
	author="Diya",
	author_email="todo@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
