"""
Module containing functions for performing various tests on the data.
"""

import math
import scipy.stats as stats
from collections import Counter
from scipy.special import gammaincc
from scipy.stats import chi2
import numpy as np
from scipy.special import chdtrc

IDENTICAL_BYTE_LIMIT = 6

def test_total_failure(probe: bytearray) -> bool:
    """
    Test if a sequence of bytes has identical bytes beyond the limit.
    Returns True if total failure detected, otherwise False.

    Parameters:
    - probe (bytearray): The sequence of bytes to test.

    Returns:
    - bool: Returns True if any byte occurs more than the limit in the probe. Returns False otherwise.

    Description:
    The function first checks if the input is of bytearray type. If not, it raises a ValueError.
    Then it counts the occurrences of each byte in the probe using a Counter from the collections module.
    It iterates over the count of each byte, and if any byte count exceeds the limit, it returns True indicating a failure.
    If no byte count exceeds the limit, it returns False indicating no failure.
    """
    if not isinstance(probe, bytearray):
        raise ValueError("Input should be of bytearray type.")
    byte_counts = Counter(probe)
    for count in byte_counts.values():
        if count > IDENTICAL_BYTE_LIMIT:
            return True
    return False


# Further Tests Implementations...
def run_tests(binary_string):
                print(binary_string)
                print("Frequency: ", frequency_test(binary_string))
                print("Runs: ", runs_test(binary_string))
                print("Serial: ", serial_test(binary_string))
                print("Poker: ", poker_test(binary_string))
                print("Cumulative: ", cumulative_sums_test(binary_string))
                print("Auto: ", autocorrelation_test(binary_string))
                print("Entropy: ", approximate_entropy_test(binary_string))
                print("Blockrun: ", longest_run_ones_in_a_block_test(binary_string))
                print("Blockfrequency: ", frequency_test_within_a_block(binary_string))
def frequency_test(binary_string):
    frequency = binary_string.count("1")
    total_bits = len(binary_string)
    return abs(frequency - total_bits / 2) / (total_bits) ** 0.5 <= 1.96


def runs_test(binary_string):
    n = len(binary_string)
    pi = binary_string.count('1') / n
    tau = 2 / (3 * n) ** 0.5

    if abs(pi - 0.5) >= tau:
        return False

    vobs = len(''.join(binary_string.split('0')).split('1')) - 1
    p_val = stats.norm.cdf((vobs - 2 * n * pi * (1 - pi)) / (2 * pi * (1 - pi) * (2 * n * pi * (1 - pi)) ** 0.5))

    if p_val < 0.01:
        return False
    else:
        return True


def poker_test(binary_string, m=4):
    n = len(binary_string)
    num_m_bit_blocks = n // m
    expected_count = num_m_bit_blocks / (2 ** m)

    blocks = [binary_string[i * m:(i + 1) * m] for i in range(num_m_bit_blocks)]
    actual_counts = Counter(blocks)
    chi_square = sum((f - expected_count) ** 2 / expected_count for f in actual_counts.values())

    return chi_square <= 9.49  # 95% confidence level, DOF=2^m-1=15


def serial_test(binary_string, m=2):
    n = len(binary_string)
    expected_count = n - m + 1
    actual_counts = Counter([binary_string[i:i + m] for i in range(n - m + 1)])
    chi_square = sum((f - expected_count) ** 2 / expected_count for f in actual_counts.values())
    return chi_square <= 9.21  # 95% confidence level, DOF=m^2-1=3


def cumulative_sums_test(binary_string):
    n = len(binary_string)
    x = [(-1) ** (int(bit) - 0.5) for bit in binary_string]
    s = np.cumsum(x)
    s_abs = np.abs(s)
    z = max(s_abs)

    # Calculate P-value
    sum_term = 0
    for k in range(-(n - 1), n):
        start = (4 * k - 1) / 4
        stop = (4 * k + 1) / 4
        sum_term += (-1) ** k * (np.exp(-2 * (start ** 2) * (z ** 2)) - np.exp(-2 * (stop ** 2) * (z ** 2)))

    p_val = 1 - sum_term

    return p_val >= 0.01  # 99% confidence


def autocorrelation_test(binary_string, d=1):
    n = len(binary_string)
    b = [int(bit) for bit in binary_string]
    b_ac = [b[i] * b[i + d] for i in range(n - d)]
    p = sum(b_ac) / (n - d) - 0.25
    v = (13 * (n - d) + 3) * 0.5 ** 2
    z = p / (v) ** 0.5
    return abs(z) <= 1.96  # 95% confidence interval


def approximate_entropy_test(binary_string, m=10):
    n = len(binary_string)
    phi_m = compute_phi(binary_string, m)
    phi_m_plus_one = compute_phi(binary_string, m + 1)
    ap_en = phi_m - phi_m_plus_one
    x = 2.0 * n * (math.log(math.factorial(m)) - math.log(math.factorial(m + 1)) - ap_en)
    p_value = gammaincc(2 ** (m - 1), x / 2.0)
    return p_value > 0.01


def compute_phi(binary_string, m):
    n = len(binary_string)
    counts = {}
    for i in range(n - m + 1):
        key = binary_string[i:i + m]
        if key not in counts:
            counts[key] = 0
        counts[key] += 1
    counts = np.array(list(counts.values()))
    return np.sum(counts * np.log(counts / float(n - m + 1)))


def longest_run_ones_in_a_block_test(binary_string):
    K = 6
    Pi = [0.2148, 0.3672, 0.2305, 0.1250, 0.0467, 0.0150, 0]
    V = np.zeros(K + 1, dtype=int)
    longest_run = 0
    current_run = 0
    for bit in binary_string:
        if bit == '1':
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            if current_run > 0:
                if current_run <= 1:
                    V[0] += 1
                elif current_run == 2:
                    V[1] += 1
                elif current_run == 3:
                    V[2] += 1
                elif current_run == 4:
                    V[3] += 1
                elif current_run == 5:
                    V[4] += 1
                else:
                    V[5] += 1
            current_run = 0
    P = np.sum(V * Pi)
    x = np.sum((V - P) ** 2 / P)
    p_value = chdtrc(K, x)
    return p_value > 0.01


def frequency_test_within_a_block(binary_string, M=100):
    n = len(binary_string)
    N = n // M
    blocks = [binary_string[i * M:(i + 1) * M] for i in range(N)]
    proportions = [(block.count('1') / M) for block in blocks]
    chi_squared = 4.0 * M * sum([(proportion - 0.5) ** 2 for proportion in proportions])
    p_value = chi2.sf(chi_squared, N)
    return p_value > 0.01
