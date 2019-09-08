# THEDEX Generator

This package generates Messages for the THEDEX API.
API Secifications can be found [at the official Sovdwaer Page](https://sovdwaer.de/files/content/dokumente/THEDEX_Entwicklerinformation.pdf).

## Build and publish
1. Create Tag & Release in Github
2. Update Download-URL in `setup.py`
3. Build and upload:

    ```bash
    $ python setup.py sdist
    $ twine upload dist/* 
    ```