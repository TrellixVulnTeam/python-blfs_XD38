from setuptools import setup

from blfs import __version__

def read_file(filename, alt=None):
    """
    Read the contents of filename or give an alternative result instead.
    """
    lines = None

    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.read()
    except IOError:
        lines = [] if alt is None else alt
    return lines



long_description = read_file('README.md', 'Cannot read README.md')
requirements = read_file('requirements.txt')


setup(
    name="BLFS-automation", 
    version=__version__,
    author="Aharon Maslin",
    author_email="aronmaslin@gmail.com",
    license='MIT',
    install_requires=requirements,
    description="BLFS automation script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahron-maslin/BLFS-automation",
    packages=['blfs'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['blfs-automation', 'blfs',
              'automation', 'education'],
    python_requires='>=3.6',
)