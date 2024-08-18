# PyCalc Documentation

## Introduction

**PyCalc** is a versatile calculator application built with Python and Tkinter. It supports both basic and scientific calculations and is designed to be user-friendly and cross-platform. This documentation provides essential information to help users get started with PyCalc, including features, installation instructions, usage guidelines, and troubleshooting tips.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division.
- **Scientific Calculations**: Square roots, exponentiation, trigonometric functions (sin, cos, tan).
- **User-Friendly Interface**: Clean and intuitive design with responsive buttons.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

## Installation

To install and use PyCalc, follow these steps:

### Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/pycalc.git

## Usage

### Basic Calculations

- **Entering Numbers**: Click on numeric buttons to input numbers.
- **Performing Operations**: Use arithmetic operation buttons (`+`, `-`, `*`, `/`) to select the desired operation.
- **Calculating Results**: Press the `=` button to compute and display the result.

### Scientific Calculations

- **Accessing Functions**: Click on buttons for scientific functions such as square roots and trigonometric functions.
- **Input Values**: Enter the required values for scientific operations.
- **Compute Results**: Press `=` to calculate and display the results.

### Error Handling

- **Division by Zero**: The calculator will display an error message if division by zero is attempted.
- **Invalid Input**: Ensure all input values and operations are valid to avoid errors.

## Architecture

PyCalc's architecture is composed of three layers:

- **User Interface (UI Layer)**: Manages user interactions and displays results.
- **Controller (Control Logic)**: Handles user input and communicates between the UI and the Calculation Engine.
- **Calculation Engine (Backend Processing)**: Performs mathematical operations and handles errors.

## Data Model

The data model includes:

- **InputBuffer**: Temporarily holds user inputs.
- **CurrentOperation**: Stores the ongoing operation.
- **Result**: Stores and displays the calculation result.

## User Stories

1. **Basic Arithmetic Operations**:
   - **As a user**, I want to perform basic arithmetic operations so that I can solve everyday mathematical problems.
   - **Acceptance Criteria**: Operations should be accurate and displayed immediately.

2. **Scientific Calculations**:
   - **As a user**, I want to perform scientific calculations to handle complex mathematical problems.
   - **Acceptance Criteria**: Scientific functions should be available and work correctly.

3. **Error Handling**:
   - **As a user**, I want the application to handle errors gracefully, like division by zero.
   - **Acceptance Criteria**: Clear error messages should be displayed, allowing continued use.

4. **User-Friendly Interface**:
   - **As a user**, I want the interface to be intuitive and easy to navigate.
   - **Acceptance Criteria**: Buttons should be well-organized, and the display should be clear and responsive.

5. **Cross-Platform Compatibility**:
   - **As a user**, I want the application to work on various operating systems.
   - **Acceptance Criteria**: The application should run smoothly on Windows, macOS, and Linux.

## Contributing

To contribute to PyCalc, please follow these steps:

1. **Fork the Repository**: Create a personal copy on GitHub.
2. **Create a Branch**: Develop changes on a new branch.
3. **Implement Changes**: Add features or fix issues.
4. **Submit a Pull Request**: Describe your changes and submit for review.

## Contact

For any questions, feedback, or support, please reach out to [medo.adel200@gmail.com].

## Acknowledgments

Special thanks to the Alx Africa , Python and Tkinter communities for their resources and support.