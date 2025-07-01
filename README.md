# Python Keylogger (Educational Purpose Only)

This project is a simple **keylogger** written in Python using the `pynput` library. It records every key pressed on the keyboard and saves the logs to a file named `keylog.txt`.

> **Warning:**  
> This tool is for educational and ethical testing purposes only.  
> **Do not use this software to invade privacy or break the law.**  
> Always get explicit permission before running a keylogger on any device.

## Features

- Logs all keystrokes (letters, numbers, special keys)
- Saves output to `keylog.txt` in the current directory
- Simple and minimal codebase

## Requirements

- Python 3.x
- [pynput](https://pypi.org/project/pynput/)

## Installation

1. **Clone or download this repository.**
2. **Install the required library:**
    ```bash
    pip install pynput
    ```

## Usage

1. **Run the script:**
    ```bash
    python keylogger.py
    ```
2. **Start typing:**  
   All keystrokes will be logged to `keylog.txt` in the same directory.
3. **Stop logging:**  
   Press `Ctrl+C` in the terminal or close the terminal window.

## How It Works

- The script uses `pynput.keyboard.Listener` to monitor keyboard events.
- Each key press is written to `keylog.txt`.
- Printable characters are logged as-is; special keys (like `Enter`, `Space`, etc.) are logged in brackets (e.g., `[Key.space]`).

## Example Output

```
hello[Key.space]world[Key.enter]
```

## Disclaimer

- This tool is intended for **educational purposes** and **authorized testing** only.
- The author is **not responsible** for any misuse or illegal activity involving this code.

## Author

- [Subham Nayak](https://github.com/Subham73-cmd)


**Use responsibly and ethically!**
