# Auto-Clicker Manager

A Python-based GUI application for automating mouse clicks, built with `tkinter`. It allows users to create, manage, and execute a sequence of mouse clicks with advanced conditions.

## Features

*   **Coordinate-based Clicking:** Specify the exact X and Y coordinates for the mouse to click.
*   **Conditional Clicking:** Optionally, trigger a click only when a specific RGB pixel color is detected at the target coordinates. This is useful for automating actions that depend on a visual cue.
*   **Click Sequence Management:**
    *   Add multiple click actions to a list to create a complex automation sequence.
    *   Remove actions from the sequence at any time.
    *   Reorder actions using "Move Up" and "Move Down" buttons to fine-tune the execution order.
*   **Real-time Mouse Information:** A live display shows the mouse cursor's current X/Y position and the RGB color of the pixel beneath it, making it easy to capture coordinates and colors.
*   **Configurable Delay:** Set a custom time delay (in seconds) that will be executed between each click in the sequence.
*   **Global Hotkeys:**
    *   **Color Picker (`Ctrl+P`):** Instantly captures the coordinates and color from the current mouse position and populates the input fields, streamlining the process of adding new click actions.
    *   **Emergency Stop (`Ctrl+Q`):** Immediately stops the clicking process and closes the application, providing a reliable way to halt the automation.
*   **Start/Stop Control:** The main window provides clear "Start" and "Stop" buttons to control the automation loop.

## Plan for Building

Building this application involves several key stages, combining a graphical user interface with background automation tasks.

1.  **Project Setup:**
    *   Choose a GUI library like `tkinter` (standard with Python) for the user interface.
    *   Install necessary third-party libraries: `pyautogui` for cross-platform mouse control and screen analysis, and `keyboard` for implementing global hotkeys.

2.  **GUI Layout (using `tkinter`):**
    *   Design and create the main application window.
    *   Add a label to display the real-time mouse position and color.
    *   Use a `Listbox` widget to display the queue of click functions.
    *   Add `Entry` widgets for user input: X, Y, R, G, B, and the time delay.
    *   Create buttons for core actions: "Add Function", "Remove Function", "Move Up", "Move Down", "Start", and "Stop".
    *   Apply styling to frames, buttons, and labels to create a clean and intuitive user interface.

3.  **Core Logic - Mouse & Screen Automation:**
    *   Implement a function that continuously tracks the mouse position and pixel color. This should run on a short timer using `root.after()` to avoid freezing the GUI.
    *   Create the main clicking loop that iterates through the list of stored functions. This loop **must** run in a separate thread (`threading`) to keep the GUI responsive while clicks are being executed.
    *   Inside the loop, for each function, use `pyautogui.pixel()` to check for color conditions (if specified).
    *   Execute the click using `pyautogui.click()`.
    *   Honor the user-defined time delay with `time.sleep()`.

4.  **State Management:**
    *   Use a Python list to store the sequence of click functions. Each function can be a dictionary containing its `x`, `y`, and `color` properties.
    *   Use a boolean flag (e.g., `self.running`) to safely start and stop the background clicking thread from the GUI.
    *   Write helper functions to add, remove, and reorder items in the list, ensuring the `Listbox` is refreshed after each change.

5.  **Global Hotkeys:**
    *   Use the `keyboard` library to listen for key presses system-wide. This listener should also run in its own background thread.
    *   Implement the `activate_color_picker` function to grab mouse data and populate the `Entry` fields when the hotkey is pressed.
    *   Implement the `stop_script` function to provide a quick-exit mechanism.

## Future Enhancements (Advanced Options)

*   **Multiple Click Types:** Add a dropdown menu to select different types of clicks (e.g., Right-Click, Double-Click, Middle-Click).
*   **Randomization:** Introduce options to slightly randomize click coordinates and time delays to better mimic human behavior, which can be useful in gaming or bot detection scenarios.
*   **Image-based Detection:** Instead of relying on a single pixel color, allow the user to select a small area of the screen and trigger a click when that image is found. This is far more robust against minor UI changes and animations.
*   **Save/Load Profiles:** Implement functionality to save a sequence of clicks to a file (e.g., in JSON format) and load it back later, allowing users to manage multiple automation tasks.
*   **Complex Macros:** Evolve the simple click sequence into a more powerful macro system that can include keyboard inputs (e.g., typing text), holding down keys, and waiting for specific images to appear on screen.
*   **Looping Control:** Add options to specify the number of times the entire sequence should loop (e.g., "Loop 10 times" or "Loop until stopped").
*   **Improved GUI:**
    *   Migrate to a more modern GUI framework or use themed `ttk` widgets for a more polished look.
    *   Add an "Always on Top" option to keep the application window visible.
    *   Provide better visual feedback, such as highlighting the currently executing step in the listbox.