# 🧮 Basic Calculator

This is a simple calculator web application built using [Streamlit](https://streamlit.io). It provides a user-friendly interface for performing basic arithmetic operations.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division.
- **Interactive Buttons**: Easy-to-use buttons for input.
- **Real-time Display**: Updates the display as you input values or perform calculations.
- **Error Handling**: Displays "Error" for invalid expressions.
- **Responsive Design**: Styled with custom CSS for a modern look.

## Installation

### For Mac/Linux:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/calculator_app.git
   cd calculator_app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### For Windows:

1. Clone the repository:
   ```cmd
   git clone https://github.com/your-username/calculator_app.git
   cd calculator_app
   ```

2. Create a virtual environment and activate it:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```cmd
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open the provided URL in your browser to access the calculator.

## How to Use

- Use the buttons to input numbers and operators.
- Press `=` to calculate the result.
- Use `C` to clear the display and `⌫` to delete the last character.

## Project Structure

```
calculator_app/
├── app.py               # Main application file
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
```

## Dependencies

- **Streamlit**: A framework for building interactive web applications in Python.