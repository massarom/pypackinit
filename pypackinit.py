"""

"""
import argparse
import datetime
import os
import sys
import warnings

SETUP_FILE = """# -*- coding: utf-8 -*-
\"\"\"Example setup.py file

This example setup file is adapted from https://github.com/pypa/sampleproject
and is not supposed to be and exahustive list of options accepted by the
setuptools' function `setup`. You should read the respective documentation,
which can be found at https://setuptools.readthedocs.io/en/latest/setuptools.html

The original License and Copyright for this setup file follows:

Copyright (c) 2016 The Python Packaging Authority (PyPA)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
\"\"\"
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name='{projectname}',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='{version}',  # Required

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description='''{short_description}''',  # Required

    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional

    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)

    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url='{url}',  # Optional

    # This should be your name or the name of the organization which owns the
    # project.
    author='{author}',  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='{author_email}',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        #'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(),  # Required

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `{projectname}`
    # which executes the function `main` from this package when invoked:
    entry_points={{  # Optional
        'console_scripts': [
            '{projectname}={projectname}:main',
        ],
    }}
)
"""
SETUP_FILE_Q = """# -*- coding: utf-8 -*-
\"\"\"Example setup.py file

This example setup file is adapted from https://github.com/pypa/sampleproject
and is not supposed to be and exahustive list of options accepted by the
setuptools' function `setup`. You should read the respective documentation,
which can be found at https://setuptools.readthedocs.io/en/latest/setuptools.html

The original License and Copyright for this setup file follows:

Copyright (c) 2016 The Python Packaging Authority (PyPA)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
\"\"\"
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='{projectname}',
    version='{version}',
    description='''{short_description}''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='{url}',
    author='{author}',
    author_email='{author_email}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        #'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    entry_points={{
        'console_scripts': [
            '{projectname}={projectname}:main',
        ],
    }}
)
"""
README_FILE = """# Welcome to {projectname}

Ahoy! I'm {author} and this is {projectname}. Thanks for stopping by! ❤

The README file will be used as a source for the long description field of your
project. The most portable markup language to use is Markdown, as it now directly supported by
PyPI and it is widely used on popular code hosting websites (like BitBucket or Github)
"""
CHANGELOG_FILE = """# {projectname}'s changelog
You should put important, human-readable changes in this file"""
LICENSE_FILE = """Copyright {date} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
MANIFEST_FILE = """include LICENSE
include CHANGELOG.md
"""

USER = os.getenv("USER", None)
EMAIL = os.getenv(
    "EMAIL", "{user}@{host}".format(user=USER, host=os.getenv("HOSTNAME", None))
)


def main():
    parser = argparse.ArgumentParser(
        prog="ppinit",
        description="Generate reasonable skeleton to start developing a python package",
    )
    parser.add_argument("project_name", help="Name of the package", type=str)
    parser.add_argument(
        "description",
        help="Short description of the package, enclosed in quotes",
        type=str,
    )
    parser.add_argument(
        "-a",
        "--author",
        help="Name of the author of the package",
        nargs="?",
        type=str,
        default=USER,
    )
    parser.add_argument(
        "-e",
        "--author-email",
        help="E-mail contact of the package's author",
        nargs="?",
        type=str,
        default=EMAIL,
    )
    parser.add_argument(
        "-u", "--url", help="URL of the project", nargs="?", type=str, default=None
    )
    parser.add_argument(
        "-q",
        "--quiet",
        help="The generated setup.py file will have way less comments",
        action="store_true",
    )
    parser.add_argument(
        "-f",
        "--force",
        help="If unset, program will exit with status 1 when a `setup.py` file is already present",
        action="store_true",
    )
    args = parser.parse_args()

    fields = dict(
        projectname=args.project_name,
        version="0.1",
        short_description=args.description,
        url=args.url,
        author=args.author,
        author_email=args.author_email,
    )
    if hasattr(parser, "author"):
        fields["author"] = args.author
    if hasattr(parser, "author_email"):
        fields["author_email"] = args.author_email
    if not args.force:
        if os.path.isfile("setup.py"):
            parser.print_help(sys.stderr)
            sys.stderr.write(
                "\nA file 'setup.py' already exists and --force was not set.\n"
            )
            sys.exit(1)

    with open("setup.py", "w", encoding="utf-8") as s:
        if not args.quiet:
            s.write(SETUP_FILE.format(**fields))
        else:
            s.write(SETUP_FILE_Q.format(**fields))
    with open("CHANGELOG.md", "w", encoding="utf-8") as cl:
        cl.write(CHANGELOG_FILE.format(projectname=args.project_name))
    with open("README.md", "w", encoding="utf-8") as rm:
        rm.write(README_FILE.format(projectname=args.project_name, author=args.author))
    with open("LICENSE", "w", encoding="utf-8") as lic:
        lic.write(
            LICENSE_FILE.format(date=datetime.datetime.today().year, author=args.author)
        )
        warnings.warn(
            "Default LICENSE file contains the MIT License text. Change it, if needed, to suit your needs!",
            Warning,
        )
    with open("MANIFEST.in", "w", encoding="utf-8") as m:
        m.write(MANIFEST_FILE)


if __name__ == "__main__":
    main()
