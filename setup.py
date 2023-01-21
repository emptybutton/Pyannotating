from setuptools import setup, find_packages


PACKAGE_NAME = 'pyannotating'

VERSION = '1.1.0'

with open('README.md') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name=PACKAGE_NAME,
    description="Library to structure annotations in your code",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license_files = ('LICENSE',),
    license="GNU General Public License v3.0",
    version=VERSION,
    url="https://github.com/TheArtur128/Pyannotating",
    download_url=f"https://github.com/TheArtur128/Pyannotating/archive/refs/tags/v{VERSION}.zip",
    author="Arthur",
    author_email="s9339307190@gmail.com",
    python_requires='>=3.11',
    classifiers=["Programming Language :: Python :: 3.11"],
    keywords=['library', 'annotations' 'generation'],
    py_modules=[PACKAGE_NAME]
)