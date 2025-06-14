from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="conversores",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Diego",
    author_email="diegoportillacosta1@gmail.com",
    description="Una librería para la conversion de unidades",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiegoPortillaC/conversor_unidades",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)