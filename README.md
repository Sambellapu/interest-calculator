# Interest Calculator Application

This repository contains a Python GUI application built using `tkinter` to calculate Simple and Compound Interest. The application provides an intuitive interface for users to select the type of interest calculation, input necessary values using a scale, and visualize the results dynamically.

## Features

- **Simple and Compound Interest Calculation**:
  - Radio buttons allow users to select between Simple and Compound Interest.
- **Interactive Input with Scales**:
  - Users can input values like principal, rate of interest, and time using scales.
- **Dynamic Results Display**:
  - The calculated interest is displayed on a scale, updated using the `.set()` method.

## Requirements

- Python 3.x
- tkinter (Standard Python library for GUI development)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/interest-calculator.git
   cd interest-calculator
   ```
2. Run the application:
   ```bash
   python interest_calculator.py
   ```

## Usage

1. **Select Interest Type**:
   - Use the radio buttons to choose either Simple Interest or Compound Interest.

2. **Input Values**:
   - Adjust the scales to input the principal amount, rate of interest, and time.

3. **View Results**:
   - The calculated interest is displayed on a separate scale.

## Example

Here is an example of how the application works:

```
Welcome to the Interest Calculator App!

Select the type of interest:
- [X] Simple Interest
- [ ] Compound Interest

Principal: [ Scale Input ]
Rate of Interest: [ Scale Input ]
Time: [ Scale Input ]

Calculated Interest: [ Scale Display with .set() method ]
```

## Program Details

- **Simple Interest Formula**:
  - SI = (P × R × T) / 100
  - Where P = Principal, R = Rate, T = Time

- **Compound Interest Formula**:
  - CI = P × (1 + R/100)^T - P

- **Dynamic Results**:
  - The results are displayed dynamically on a scale using the `.set()` method for real-time feedback.

## Future Improvements

- Add a feature to save calculated results for future reference.
- Include graphical representations of interest growth over time.
- Add support for more complex financial calculations.
- Make the application mobile-friendly.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Pavan, for the idea of creating this interest calculator.
- Python community, for the tools and resources.

---

Start Calculating with Ease! 🧮

