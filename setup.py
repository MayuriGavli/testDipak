# from setuptools import setup, find_packages
# from typing import List

# hypen = "-e ."
# def get_requirements(file_path: str) -> List[str]:
#     requirements=[]
#     with open(file_path) as file:
#         requirements=file.readlines()
#         requirements = [line.strip() for line in requirements ]
#         if hypen in requirements:
#             requirements.remove(hypen)
#     return requirements

# setup(
#     name="mlproject",
#     version="0.0.1",
#     description="This is MR's first ML project.",
#     author="MR",
#     author_email="mrgavli9@gmail.com",
#     packages=find_packages(),  # Automatically find sub-packages
#     install_requires=get_requirements("requirements.txt"),
# )


from setuptools import setup, find_packages
from typing import List

# Removed redundant hypen, made the function more generic.
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [line.strip() for line in requirements ]  # Remove empty lines
        if "-e ." in requirements:
            requirements.remove("-e .")  # Remove the local editable install bcz we just have to access the library only
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    description="This is MR's first ML project.",
    author="MR",
    author_email="mrgavli9@gmail.com",
    packages=find_packages(),  # Automatically find sub-packages
    install_requires=get_requirements("packages.txt"),
)
