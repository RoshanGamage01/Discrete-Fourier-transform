import numpy as np
from tqdm import tqdm

def dft(signal_data : np.ndarray, sample_rate: int) -> dict :
    sample_size = signal_data.size
    max_frequency = sample_size // 2

    dft_coefficients = np.zeros(max_frequency, dtype=complex)

    for k in tqdm(range(max_frequency), desc='Calculating DFT Coefficients'):
        kth_coefficient = 0

        for n in range(sample_size):
            kth_coefficient += signal_data[n] * np.exp(-2j * np.pi * k * n / sample_size)

        dft_coefficients[k] = kth_coefficient
    
    return {
        'dft_coefficients': dft_coefficients,
        'sample_rate': sample_rate
    }

def idft(dft_coefficients : np.ndarray, sample_size: int) -> np.ndarray:
    idft_values = np.zeros(sample_size, dtype=complex)

    for n in tqdm(range(sample_size), desc='Calculating IDFT Values'):
        nth_value = 0

        for k in range(len(dft_coefficients)):
            nth_value += dft_coefficients[k] * np.exp(2j * np.pi * k * n / sample_size)

        idft_values[n] = nth_value / sample_size

    return idft_values