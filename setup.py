import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sdc_py",
    version="1.3.9",
    author="dudoska",
    author_email="me@dudosa.dev",
    license="MIT License",
    platforms="OS Independent",
    url="https://github.com/dudoska/sdc-py",
    description="An async wrapper for server-discord.com API (fork of sdc_api_py by @TheKing-OfTime)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">= 3.7",
)

### python -m build