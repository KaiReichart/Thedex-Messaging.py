import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Thedex_Messaging",
    version="0.0.1",
    author="Kai Reichart",
    author_email="kai@reichart.dev",
    description="A Package to create Messages for the Thedex_Messaging API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KaiReichart/Thedex-Messaging.py",
    download_url="",
    packages=setuptools.find_packages(),
    install_requires=[            # I get to this in a second
          'datetime',
      ],
    classifiers=[
        "Development Status :: 4 - Beta"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)