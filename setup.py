from setuptools import setup, find_packages


setup(
    name="rss_reader",
    version="0.0.1",
    description="Searching and reading aricles from feeds",
    long_description="RSS feed reader for searching and reading aricles",
    url="https://github.com/terrasea/rss_reader",
    author="James Hurford",
    author_email="terrasea@gmail.com",
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Other Audience",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    keywords="rss reader article search filter",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
)
