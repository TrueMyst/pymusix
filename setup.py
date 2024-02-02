import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
desc = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pymusix",
    version="1.0.0",
    description="🌿 Retrieve information about a song, including details like the artist, album, release date, genres, and lyrics using Spotify and MusixMatch API",
    long_description=desc,
    long_description_content_type="text/markdown",
    author="TrueMyst",
    url="https://github.com/TrueMyst/pymusix",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    packages=find_packages(include=["pymusix"]),
)
