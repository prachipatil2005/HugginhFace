# Question Answering System Using Hugging Face

This project is a simple Question Answering (QA) system built using the Hugging Face `transformers` library and a graphical user interface (GUI) created with `tkinter`. The system uses a pre-trained BERT model to answer questions based on a given context.

## Features

- Input context and question through a user-friendly GUI.
- Get answers to questions using the Hugging Face QA pipeline.
- Error handling for empty context or question inputs.

## Requirements

- Python 3.6+
- `tkinter` library (usually included with Python)
- `transformers` library from Hugging Face

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install transformers
    ```

## Usage

1. Run the [main.py](http://_vscodecontentref_/0) script:
    ```sh
    python main.py
    ```

2. Enter the context in the "Context" text area.
3. Enter the question in the "Question" input field.
4. Click the "Get Answer" button to generate the answer.
5. The answer will be displayed below the button.

## File Structure

- [main.py](http://_vscodecontentref_/1): The main script that initializes the GUI and handles the QA process.

## Example

1. Enter the following context:
    ```
    The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower.
    ```

2. Enter the following question:
    ```
    Who designed the Eiffel Tower?
    ```

3. Click "Get Answer" and the system will display:
    ```
    Answer: Gustave Eiffel
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
