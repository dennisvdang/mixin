==============================
![Static Badge](https://img.shields.io/badge/Project_Status-In_Progress-orange)

# Mixin
AI-powered DJ that generates mixtapes from a playlist of songs.

## Project Organization
------------
```markdown
    mixin
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   │   └── audio_files
    │   │       ├── processed <- Place processed audio files here
    │   │       └── raw       <- Place raw audio files here
    │   └── raw            <- The original, immutable data dump.
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   ├── data           <- Scripts to download or generate data
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │                     predictions
    └── tests              <- Unit tests for the project's source code
```

## Installation
To set up your environment to run the code in this project, follow these steps:

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.

## Usage
- Place your raw audio data in `data/raw` and processed audio data in `data/processed/audio_files/processed`.
- Run Jupyter notebooks in the `notebooks/` directory for data analysis and exploration.
- Use scripts in the `src/` directory for data processing, feature extraction, and model training.

## Contributing
Contributions to this project are welcome. Please refer to the `CONTRIBUTING.md` file for guidelines.

## License
This project is licensed under the terms of the `LICENSE` file.

--------
