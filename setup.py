import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="htmltable2csv",
    version="0.5.0",
    author="Aqib",
    author_email="aqib@codecrud.com",
    description="Transform HTML tables in a Web Page to CSV files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aqib-git/htmltable2csv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)