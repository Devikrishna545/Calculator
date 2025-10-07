# Calculator App

A Python-based calculator application with both GUI and console interfaces, built using Tkinter and following MVC (Model-View-Controller) architecture pattern.

## 📋 Features

### Basic Operations
- ✅ Addition (+)
- ✅ Subtraction (-)
- ✅ Multiplication (*)
- ✅ Division (/)

### Advanced Operations
- 🔢 Square Root (√)
- 📊 Percentage (%)
- 💾 Memory Functions (M+, M-, Memory Store/Recall)

### Interface Options
- 🖥️ **GUI Interface**: Modern Tkinter-based calculator with button layout
- 💻 **Console Interface**: Command-line calculator for quick calculations

## 🏗️ Project Structure

```
Calculator/
├── app.py                    # Main application entry point
├── Calculator.py             # Console-based calculator implementation
├── README.md                 # This file
└── src/
    ├── __init__.py
    ├── controller/
    │   ├── __init__.py
    │   └── calc_controller.py # Controller logic (MVC pattern)
    ├── model/
    │   ├── __init__.py
    │   ├── simple_calc.py     # Basic arithmetic operations
    │   └── special_calc.py    # Advanced operations & memory functions
    └── view/
        ├── __init__.py
        └── Mainwindow.py      # GUI implementation using Tkinter
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Devikrishna545/Calculator.git
cd Calculator
```

2. No additional dependencies required! The calculator uses only Python standard library.

### Running the Application

#### GUI Calculator (Recommended)
```bash
python app.py
```

#### Console Calculator
```bash
python Calculator.py
```

## 💡 Usage

### GUI Interface
1. Launch the GUI calculator using `python app.py`
2. Use the on-screen buttons to input numbers and operations
3. Press `=` to calculate results
4. Use `C` to clear the display
5. Memory functions:
   - `M+`: Add current value to memory
   - `M-`: Subtract current value from memory

### Console Interface
1. Run `python Calculator.py`
2. Enter the first number
3. Choose an operator: `+`, `-`, `*`, `/`, `sqt` (square root), `%` (percentage)
4. For basic operations, specify how many numbers to operate on
5. Enter additional numbers as prompted
6. Press `=` to get the result

## 🏛️ Architecture

The project follows the **MVC (Model-View-Controller)** design pattern:

- **Model** (`src/model/`): Contains business logic
  - `SimpleCalculator`: Basic arithmetic operations
  - `SpecialCalculator`: Advanced operations and memory management

- **View** (`src/view/`): User interface components
  - `Mainwindow.py`: Tkinter-based GUI implementation

- **Controller** (`src/controller/`): Manages communication between Model and View
  - `CalcController`: Coordinates operations between model and view

## 🔧 Technical Details

### Classes Overview

#### SimpleCalculator
```python
- add(a, b): Addition operation
- sub(a, b): Subtraction operation  
- mul(a, b): Multiplication operation
- div(a, b): Division operation (with zero-division protection)
```

#### SpecialCalculator
```python
- sqrt(a): Square root calculation
- perct(a): Percentage calculation
- memory_store(c): Store value in memory
- mem_recall(): Recall stored memory value
- mem_add(a): Add value to memory
- mem_sub(a): Subtract value from memory
```

## 🎯 Example Usage

### Basic Calculation
```
Input: 15 + 25
Output: 40

Input: 100 - 30
Output: 70

Input: 8 * 7
Output: 56

Input: 84 / 12
Output: 7.0
```

### Advanced Operations
```
Square Root of 16: 4.0
25% of 200: 50.0
```

## 🐛 Known Issues

- Console interface has some incomplete functionality in multi-number operations
- GUI calculator button event handling could be improved
- Error handling could be enhanced for edge cases

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Scientific calculator functions (sin, cos, tan, log, etc.)
- [ ] History/previous calculations display
- [ ] Keyboard input support for GUI
- [ ] Unit tests implementation
- [ ] Error handling improvements
- [ ] Themes and customization options

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Devikrishna545**
- GitHub: [@Devikrishna545](https://github.com/Devikrishna545)

---

⭐ If you found this project helpful, please give it a star!
