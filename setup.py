"""
packaging module to install: python.exe -m pip install --upgrade setuptools wheel
to create the tar.gz: python.exe setup.py sdist
to create the weels: python.exe setup.py sdist bdist_wheel --universal
"""

import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

def install_required():
  return [line for line in open('requirements.txt')]

setuptools.setup(
    name="epyk-flask",
    author="epykure",
    version="1.00.00",
    author_email="smith.pyotr@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/epykure/epyk-engine",
    packages=setuptools.find_packages(),
    install_requires=install_required(),
    # package_data={'epyk': [os.path.join('static', 'images', '*'), os.path.join('static, 'images', 'logo', '*')]},
    # entry_points={"console_scripts": ["epyk-engine = epyk_server.system.cli.command_line_fncs:main"]},
    python_requires=">=2.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
)