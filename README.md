# Auto-Clicker Manager

This is a powerful GUI application for automating mouse clicks, built with Python and `tkinter`. It allows users to create, manage, and execute a sequence of mouse clicks with advanced conditions, including color and image detection.

## Features

*   **Multiple Detection Modes:**
    *   **Coordinate-based Clicking:** Specify the exact X and Y coordinates for the mouse to click.
    *   **Color-based Clicking:** Trigger a click only when a specific RGB pixel color is detected at the target coordinates.
    *   **Image-based Clicking:** Capture a region of the screen and trigger a click when that image is found. This is highly robust against UI changes.
*   **Flexible Click Types:** Perform Left, Right, or Double-clicks for any action.
*   **Full Sequence Control:**
    *   Add, remove, and reorder actions in a sequence.
    *   Set a custom time delay (in seconds) between clicks.
    *   Configure the number of times the entire sequence should loop (0 for infinite).
*   **Save/Load Profiles:** Save complex click sequences to a file and load them back later. This feature embeds images directly into the profile, making them fully portable.
*   **User-Friendly Tools:**
    *   **"Test Action" Button:** Safely check if an action's condition (color or image) is met without performing a click.
    *   **Live Progress Bar:** The currently executing action is highlighted in the list, providing a clear visual indicator of the clicker's progress.
    *   **Always on Top:** An option to keep the application window visible over all others.
*   **Global Hotkeys:**
    *   `Ctrl+S`: Stop the clicking sequence without closing the app.
    *   `Ctrl+P`: Instantly capture the mouse coordinates and pixel color.
    *   `Ctrl+Q`: Immediately stop everything and exit the application.

## How to Create the Application (for Users)

Follow these two simple steps to create the final, double-clickable application on your computer.

### Step 1: Install Dependencies

Run the installation script for your operating system. This will automatically install all the necessary packages.

*   **On Windows:** Double-click the `install_dependencies.bat` file.
*   **On macOS/Linux:** Open a terminal, navigate to this folder, and run the command: `./install_dependencies.sh`

### Step 2: Package the Application

After the installation is complete, run the packaging script for your operating system.

*   **On Windows:** Double-click the `package_app.bat` file.
*   **On macOS/Linux:** Open a terminal, navigate to this folder, and run the command: `./package_app.sh`

This will create a new folder named `dist` in the same directory as the project files. Inside `dist`, you will find the final, standalone application (`Clicker.exe` on Windows or `Clicker` on macOS/Linux) that you can run or share.

**Note for Windows users:** A shortcut to the application will also be automatically created on your Desktop for your convenience.