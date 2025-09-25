# Auto-Clicker Manager
**Author:** Fire Eagle

This is a powerful GUI application for automating mouse clicks, built with Python. It allows users to create, manage, and execute a sequence of mouse clicks with advanced conditions. The final executable will have "Fire Eagle" embedded as the publisher in its file properties.

## Features

*   **Multiple Detection Modes:**
    *   **Coordinate-based Clicking:** Specify the exact X and Y coordinates for the mouse to click.
    *   **Color-based Clicking:** Trigger a click only when a specific RGB pixel color is detected at the target coordinates.
*   **Full Sequence Control:**
    *   Add, remove, and reorder actions in a sequence.
    *   Set a custom time delay (in seconds) between clicks.
*   **Global Hotkeys:**
    *   `Ctrl+P`: Instantly capture the mouse coordinates and pixel color.
    *   `Ctrl+Q`: Immediately stop everything and exit the application.

## How to Create the Application (for Developers)

This project uses a standard Python virtual environment to ensure a clean and reliable build process. Follow these two simple steps to create the final, double-clickable application on your computer.

### Step 1: Run the Setup Script

This will create a self-contained Python environment and install all the necessary packages. Run the script for your operating system:

*   **On Windows:** Double-click `setup.bat`
*   **On macOS/Linux:** Open a terminal, navigate to this folder, and run the command: `./setup.sh`

### Step 2: Run the Packaging Script

After the setup is complete, this script will build the final application.

*   **On Windows:** Double-click `package.bat`
*   **On macOS/Linux:** Open a terminal, navigate to this folder, and run the command: `./package.sh`

Once finished, a new folder named **`dist`** will be created in the project directory. Inside `dist`, you will find the final, standalone application (`Clicker.exe` on Windows or `Clicker` on macOS/Linux).

---

## How to Distribute to Users (GitHub Release)

For the best user experience, you should upload the final `.exe` (or application file) to a GitHub Release. This allows users to download a single file instead of all the source code.

1.  After running the packaging script, find the final application in the `dist` folder.
2.  On your GitHub repository page, click on "Releases" on the right sidebar.
3.  Click "Create a new release" or "Draft a new release".
4.  Give it a version number (e.g., `v1.0`).
5.  In the "Attach binaries" section, upload the `Clicker.exe` (or `Clicker`) file from your `dist` folder.
6.  Publish the release.

Now your users can download the application with a single click!