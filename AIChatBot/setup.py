from setuptools import setup, find_packages

VERSION = '0.0.Dev1'
DESCRIPTION = 'AIChatBot'
LONG_DESCRIPTION = 'AI Chat Bot'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="AIChatBot",
    version=VERSION,
    author="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'AIChatBot'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)