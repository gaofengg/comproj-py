## Project description

compyc is a tool for compiling Python projects into pyc binary packages.

What can be done?

- Compile the specified project separately.

- Bulk compiles all projects in the specified directory.

## Installing

Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/):

`$ pip install click`

Click supports Python 3.6 and newer.

## A Simple Example

What does it look like? Here is an example of a simple compyc program:

```
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src/
│   └── example_package/
│       ├── __init__.py
│       └── example.py
└── tests/
```

The projects path:

```
/User/username/Documents/python_projects/packaging_tutorial_1
/User/username/Documents/python_projects/packageing_tutorial_2
```

```bash
$ cd /User/username/Documents/python_projects
# Compile the specified project separately.
$ compyc -p packaging_tutorial_1 -v 0.1.0
$ ls
packaging_tutorial_1 packaging_tutorial_1-0.1.0 packaging_tutorial_2

# Bulk compiles all projects in the specified directory.
$ compyc -v 0.1.0
# or
$ compyc -p /User/username/Documents/python_projects/ -v 0.1.0
$ ls
packaging_tutorial_1 packaging_tutorial_1-0.1.0 
packaging_tutorial_2 packaging_tutorial_2-0.1.0
```

A description of the parameter -p:

**-p is followed by a path value**

- When the path value ends with "/", the program treats the path as a directory, and each folder in the directory is treated as a separate project, and subsequent actions are iteratively compiled for each project in the directory.

- When the path ends without a "/", the specified path is treated as a stand-alone project.

- When the -p parameter is omitted, the default path value is ".", which is the current directory, and all projects under the current project are iteratively compiled.



## Links

- Project URL: [Click | The Pallets Projects](https://github.com/gaofengg/compyc)
