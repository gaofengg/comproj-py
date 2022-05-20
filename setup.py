from setuptools import find_packages, setup

setup(
    name='comproj-py',
    version='0.1.0',
    package=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        compy=comprojpy.compy:compile 
    """,
)
