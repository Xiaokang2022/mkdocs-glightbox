
from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mkdocs-glightbox",
    version="0.1.0",
    author="Blueswen",
    author_email="blueswen.tw@gmail.com",
    packages=find_packages(),
    license="LICENSE.md",
    description="MkDocs plugin supports image lightbox with GLightbox.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4>=4.11.1"
    ],
    package_data={
        "mkdocs_glightbox": ["glightbox/*"],
    },
    entry_points={
        "mkdocs.plugins": [
            "glightbox = mkdocs_glightbox:LightboxPlugin",
        ]
    }
)