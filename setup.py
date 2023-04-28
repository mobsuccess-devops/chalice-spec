import pathlib

import pkg_resources
import setuptools

LIBRARY_NAME = "mobsuccess-chalice-spec"
MAINTAINER = "tech@mobsuccess.com"

with open("README.md", "r") as fh:
    long_description = fh.read()

with pathlib.Path("requirements.txt").open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

setuptools.setup(
    name=LIBRARY_NAME,
    version="0.4.0",
    author="Mobsuccess",
    author_email=MAINTAINER,
    description="mobsuccess python data-access library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mobsuccess-devops/chalice-spec",
    packages=setuptools.find_packages(),
    package_data={
        LIBRARY_NAME: ["*.pyi", "**/*.pyi"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    setup_requires=["wheel"],
    install_requires=install_requires,
)
