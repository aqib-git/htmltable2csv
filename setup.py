import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="table2csv",
    version="0.4.0",
    author="Aqib",
    author_email="aqib@codecrud.com",
    description="Convert HTML tables in a Web Page to CSV files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aqib-git/table2csv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)