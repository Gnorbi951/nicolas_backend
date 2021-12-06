"""Setup for map evaluator"""
import psycopg2
import setuptools

with open("README.md", "r", encoding="utf8") as f:
    long_description = f.read()

setuptools.setup(
    name="nicolas_cage_webshop_backend",
    description="Backend API service for nicolas_cage_frontend",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Norbert Gocze",
    author_email="gnorbi951@gmail.com",
    url="https://github.com/Gnorbi951/nicolas_backend",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    # This is a string list of dependent packages.These packages are installed automatically with pip,
    # requirements.txt is redundant.
    install_requires=["flask", "psycopg2-binary"],
    setup_requires=['setuptools_scm'],
    # These dependencies won't be installed unless specified like: `pip install nicolas_cage_webshop_backend[test]`
    # Previously `tests_require` could be used but it is now deprecated.
    extras_require={},
    # The folder must be a git repository otherwise version cannot be read.
    # The version starts from 0.1 and automatically read from git tags if there are x.y.z tags,
    # where x, y, and z are integers. You can try it by `python setup.py --version`
    # Please use annotated tags for versioning. (`git tag -a TAG`)
    use_scm_version=True,
    # With this may not work on windows because of the directory separator difference.
    # It can be resolved with os.path.join, but the entry_points method is easier.
    scripts=[],
    entry_points={
        'console_scripts': [
            "webserver = main.py:main",
        ],
    }
)
