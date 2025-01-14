# Python Package Initializer

> [!IMPORTANT]
> This package is not useful anymore, as many solid projects have sprouted that make initialising
> a new package extremely easy. My current favourite is [uv](https://docs.astral.sh/uv/).

This utility is aimed at creating the boilerplate necessary when starting a new python package.
I've found out that packaging even my own script helps tremendously in the long run, and also
improves the general quality of my projects.

## How do I install it?

Simply open a terminal/prompt and type
```sh
pip install pypackinit
```
and a new command, `ppinit` will be added to your `PATH`.

If you can't install packages in your system interpreter (you shouldn't anyway), you can add the `--user` option.

## What does this script do?

Following the PyPA guide on packaging, this script simply generates the essential files
to get you started on a new project. Suppose you want to start a project named `panino`.
This means that you have to create by hand the `setup.py` script, fill it up, then create
`README`, `CHANGELOG`, `LICENSE`, etc. With `pypackinit`, all of this is done with a single
line (spread on multiple lines for clarity).

    ppinit panino 'The best panino on Earth, with even more cheese!' \
        -a 'Nino Pa' \
        -e ninopa@bread.com \
        -u https://panino.bread.com

Now you have a directory structure like this

    project_root/
    ├── panino
    │   └── __init__.py
    ├── CHANGELOG.md
    ├── LICENSE.txt
    ├── MANIFEST.in
    ├── README.md
    └── setup.py

ready to go! In practice, this script is an extremely simplified version of
[cookiecutter](https://github.com/audreyr/cookiecutter/) (and it's _not_ a fork).

## Why packaging my own modules?

Packaging means that you don't have to set up your `PYTHONPATH` every time you change machine and
that your virtualenvs can simply "install" your other projects.

Suppose that you have `Project A` and `Project B`, where `B` depends on `A`. With packaging, you
could install `A` in `B`'s virtual environment and then you could fix issues and work on additional
features of `A` without compromising the functionality of `B`. I have had this issue several times
and by pacakging basically all my scripts and modules I have solved most of my problems when it
comes to re-use my projects!

Also, I found out that sharing code with people that are not comfortable with `git` and the likes
is way easier if you can just send them a `wheel`. :)
