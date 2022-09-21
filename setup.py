import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    README = fh.read()

setuptools.setup(
    name="splitter",
    version="0.0.1",
    author="Peter Horvat",
    author_email="peter.horvat85@gmail.com",
    description="Document splitter",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/peterhorvat/Splitter",
    project_urls={
        "Bug Tracker": "https://github.com/peterhorvat/Splitter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8"
)
