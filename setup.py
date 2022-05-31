from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="compyc",
    version="0.1.26",
    author="GaoFeng",
    author_email="ymmtd@163.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaofengg/compyc",
    project_urls={
        "Bug Tracker": "https://github.com/gaofengg/compyc/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        compyc=compyc.compyc:compile 
    """,
)
