from setuptools import find_packages, setup

setup(
    name='compyc',
    version='0.1.24',
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
