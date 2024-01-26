from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
desc = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pymusix",
    version="0.0.1",
    description="PyMusix is a Python package designed to retrieve information about a song, including details like the artist, album, release date, genres, and lyrics. The package utilizes the Spotify and Musixmatch APIs to gather this information.",
    long_description=desc,
    long_description_content_type="text/markdown",
    author="TrueMyst",
    url="https://github.com/TrueMyst/pymusix",
    license="Apache",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    packages=find_packages(include=["pymusix", "pymusix.*"]),
)
