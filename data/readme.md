# Data Directory README

Welcome to the `data` subfolder. This directory contains various types of data crucial for the SALAMI dataset, including annotations, audio files (not publicly available), dataframes, and reference materials.

## Contents

### `annotations/`
This directory contains the annotation files for the music pieces in the SALAMI dataset. Annotations are organized by song, with each song's annotation data stored in a distinct folder named by its `song_id`. Inside each `song_id` folder, you will find:

- `textfile1.txt`: The primary annotation file for the song, provided by the first annotator.
- `textfile2.txt`: (If available) The secondary annotation file for the song, provided by the second annotator. Note that not all songs have annotations from two different annotators.

Each `song_id` folder also contains a `parsed` subfolder, which includes parsed versions of the raw annotation data:

- `parsed/`: This subfolder contains parsed annotation data from `textfile1.txt` and, if available, `textfile2.txt`. Our analysis only used the function parsed files, which are named using the convention `textfile[annotator_id]_functions.txt` and contain the label data that indicate the functional segments within the song and their associated timestamps. 

The `SALAMI Annotator Guide.pdf` in the `reference/` directory provides detailed information on the annotation format and how to interpret the parsed data.
## Data Use

### `audio_files/`
Here you will find the audio files corresponding to the annotations.

- `processed/`: Contains audio files that have been processed and are ready for analysis.
- `raw/`: Contains the original, unprocessed audio files as they were collected or received before any analysis or processing.
- `segmented/`: Contains segmented audio files. 

### `dataframes/`
This directory includes CSV files or other data file formats that contain dataframes. These dataframes are generated from various data cleaning/processing/analysis done through computational notebooks and represent structured data that can be easily manipulated for further study.

### `reference/`
External reference materials are stored here. These may include documents, guides, and supplementary data that provide additional context or information necessary for understanding or conducting analyses on the SALAMI dataset. Notably, this folder includes the `SALAMI Annotator Guide.pdf`, which details the format for parsing and understanding the annotations.

## Data Use

For information on how to use this data within the context of the SALAMI project, please refer to the documentation in the root directory of this repository.

## License

The data contained within this directory is released under the Creative Commons 0 license, allowing for the data to be used freely with no restrictions.

## Contact

For any questions regarding the data or its use, please refer to the contact information provided in the main README file of the repository, or visit the SALAMI project's official communication channels.