# Audio Signal Processing

This repository contains Python scripts for performing Discrete Fourier Transform (DFT) and Inverse Discrete Fourier Transform (IDFT) on audio signals. The project includes functionality to visualize the frequency spectrum of an audio signal and save the processed audio back to a file.

## Project Structure

- [`audio_signal/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Faudio_signal%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "/Users/roshangamage/projects/Fourier Transform/Discrete-Fourier-transform/audio_signal/"): Directory containing audio files.
- [`dft.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Fdft.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "/Users/roshangamage/projects/Fourier Transform/Discrete-Fourier-transform/dft.py"): Contains functions for DFT and IDFT.
- [`index.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Findex.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "/Users/roshangamage/projects/Fourier Transform/Discrete-Fourier-transform/index.py"): Main script to process audio files.
- [`util.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Futil.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "/Users/roshangamage/projects/Fourier Transform/Discrete-Fourier-transform/util.py"): Utility functions for audio file operations.
- [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "/Users/roshangamage/projects/Fourier Transform/Discrete-Fourier-transform/requirements.txt"): List of dependencies.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/RoshanGamage01/Discrete-Fourier-transform.git
    cd Discrete-Fourier-transform
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place your audio file in the [`audio_signal/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Faudio_signal%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "/Users/roshangamage/projects/Fourier Transform/Discrete-Fourier-transform/audio_signal/") directory.

2. Run the main script:
    ```sh
    python index.py
    ```

3. The script will:
    - Read the audio file.
    - Perform DFT to compute the frequency spectrum.
    - Plot the frequency spectrum.
    - Perform IDFT to reconstruct the audio signal.
    - Save the reconstructed audio signal to [`idft_output.wav`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Fidft_output.wav%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "/Users/roshangamage/projects/Fourier Transform/Discrete-Fourier-transform/idft_output.wav").

## Functions

### [`dft.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Fdft.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "/Users/roshangamage/projects/Fourier Transform/Discrete-Fourier-transform/dft.py")

- [`dft(signal_data: np.ndarray, sample_rate: int) -> dict`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Fdft.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Findex.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A5%7D%7D%5D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "Go to definition")
    - Computes the Discrete Fourier Transform of the input signal.
    - Returns a dictionary containing DFT coefficients and the sample rate.

- [`idft(dft_coefficients: np.ndarray, sample_size: int) -> np.ndarray`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Fdft.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A22%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Findex.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A30%2C%22character%22%3A14%7D%7D%5D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "Go to definition")
    - Computes the Inverse Discrete Fourier Transform of the DFT coefficients.
    - Returns the reconstructed time-domain signal.

### [`util.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Futil.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "/Users/roshangamage/projects/Fourier Transform/Discrete-Fourier-transform/util.py")

- [`save_as_audio_file(idft_values: np.ndarray, sample_rate: int, file_name: str)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Findex.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A31%2C%22character%22%3A0%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Futil.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A4%7D%7D%5D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "Go to definition")
    - Saves the IDFT values as an audio file.

## Dependencies

- [`numpy`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Fdft.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Findex.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Futil.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A7%7D%7D%5D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "Go to definition")
- [`matplotlib`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Findex.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A0%7D%7D%5D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "Go to definition")
- [`wave`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Findex.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Futil.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A0%7D%7D%5D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "Go to definition")
- [`tqdm`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Fdft.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Froshangamage%2Fprojects%2FFourier%20Transform%2FDiscrete-Fourier-transform%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A0%7D%7D%5D%2C%224b935bb3-f611-4e62-8f41-75b20c7e6fa3%22%5D "Go to definition")

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [TQDM](https://tqdm.github.io/)
