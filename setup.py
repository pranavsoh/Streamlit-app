from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


AUTHOR_NAME = "Pranav Soahney"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["streamlit"]


setup(
    name=SRC_REPO,
    version="0.0.1",
    author_email= "pranavsohaney90@gmail.com",
    description="A sample example package for movies recommendation project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package= [SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS,

    )