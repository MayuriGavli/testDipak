from setuptools import find_packages,setup

setup(
    name="Mayuri",
    version="0.0.1",
    description="This is MR first ml Project.",
    author="MR",
    author_email="mrgavli9@gmail.com",
    packages=find_packages(),
    install_requires = ['pandas','numpy','seaborn'],
)