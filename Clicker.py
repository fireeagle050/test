# Import necessary libraries
import tkinter as tk  # For creating the GUI
from tkinter import messagebox, filedialog  # For showing messages and opening file dialogs
import pyautogui  # For controlling the mouse and screen
import threading  # For running tasks in the background
import time  # For adding delays
import keyboard  # For detecting global hotkeys
import json  # For saving and loading profiles

# Main application class
class AutoClickerApp:
    # Constructor for the class
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title("Auto-Clicker Manager")  # Window title
        self.root.geometry("700x700")  # Window size
        self.root.configure(bg="#282c34")  # Window background color

        # Initialize variables
        self.click_functions = []  # List to store click sequences
        self.running = False  # Flag to check if the clicker is running
        self.time_delay = 1  # Default time delay between clicks
        self.loop_count = 0  # Default loop count (0 for infinite)

        # Set up the user interface
        self.setup_ui()
        # Start updating the mouse position display
        self.update_mouse_position()
        # Set up global hotkeys
        self.setup_global_shortcuts()

    # Method to set up the UI
    def setup_ui(self):
        # Define styles for UI elements
        label_font = ("Arial", 12, "bold")
        entry_bg = "#1e1e1e"
        entry_fg = "#ffffff"
        button_bg = "#61afef"
        button_fg = "#ffffff"
        frame_bg = "#282c34"
        entry_borderwidth = 2
        entry_relief = "solid"

        # Create a menubar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        # Create a "File" menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save Profile", command=self.save_profile)
        file_menu.add_command(label="Load Profile", command=self.load_profile)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.stop_script)
        menubar.add_cascade(label="File", menu=file_menu)
        # Create an "Options" menu
        options_menu = tk.Menu(menubar, tearoff=0)
        self.always_on_top_var = tk.BooleanVar()
        options_menu.add_checkbutton(label="Always on Top", onvalue=True, offvalue=False, variable=self.always_on_top_var, command=self.toggle_always_on_top)
        menubar.add_cascade(label="Options", menu=options_menu)

        # Create a label to display the mouse position
        self.mouse_position_label = tk.Label(
            self.root,
            text="Mouse Position: X=0, Y=0, Color=(0, 0, 0)",
            font=("Arial", 10),
            bg="#282c34",
            fg="#abb2bf",
        )
        self.mouse_position_label.pack(pady=10)

        # Create a listbox to display the click sequence
        self.listbox = tk.Listbox(self.root, width=90, height=15, bg="#1e1e1e", fg="#dcdcdc", font=("Arial", 10))
        self.listbox.pack(pady=10)

        # Create a frame for the input fields
        form_frame = tk.Frame(self.root, bg=frame_bg)
        form_frame.pack(pady=10)

        # Create input fields for X, Y, and RGB values
        tk.Label(form_frame, text="X:", font=label_font, bg=frame_bg, fg="#dcdcdc").grid(row=0, column=0, padx=5)
        self.x_entry = tk.Entry(form_frame, width=10, bg=entry_bg, fg=entry_fg, borderwidth=entry_borderwidth, relief=entry_relief)
        self.x_entry.grid(row=0, column=1, padx=5)

        tk.Label(form_frame, text="Y:", font=label_font, bg=frame_bg, fg="#dcdcdc").grid(row=0, column=2, padx=5)
        self.y_entry = tk.Entry(form_frame, width=10, bg=entry_bg, fg=entry_fg, borderwidth=entry_borderwidth, relief=entry_relief)
        self.y_entry.grid(row=0, column=3, padx=5)

        tk.Label(form_frame, text="R:", font=label_font, bg=frame_bg, fg="#dcdcdc").grid(row=1, column=0, padx=5)
        self.r_entry = tk.Entry(form_frame, width=10, bg=entry_bg, fg=entry_fg, borderwidth=entry_borderwidth, relief=entry_relief)
        self.r_entry.grid(row=1, column=1, padx=5)

        tk.Label(form_frame, text="G:", font=label_font, bg=frame_bg, fg="#dcdcdc").grid(row=1, column=2, padx=5)
        self.g_entry = tk.Entry(form_frame, width=10, bg=entry_bg, fg=entry_fg, borderwidth=entry_borderwidth, relief=entry_relief)
        self.g_entry.grid(row=1, column=3, padx=5)

        tk.Label(form_frame, text="B:", font=label_font, bg=frame_bg, fg="#dcdcdc").grid(row=1, column=4, padx=5)
        self.b_entry = tk.Entry(form_frame, width=10, bg=entry_bg, fg=entry_fg, borderwidth=entry_borderwidth, relief=entry_relief)
        self.b_entry.grid(row=1, column=5, padx=5)

        # Create a dropdown menu for the click type
        tk.Label(form_frame, text="Click Type:", font=label_font, bg=frame_bg, fg="#dcdcdc").grid(row=2, column=0, padx=5, pady=5)
        self.click_type_var = tk.StringVar(value="Left")
        click_type_options = ["Left", "Right", "Double"]
        self.click_type_menu = tk.OptionMenu(form_frame, self.click_type_var, *click_type_options)
        self.click_type_menu.config(bg=button_bg, fg=button_fg, font=("Arial", 10), relief="raised", bd=3)
        self.click_type_menu.grid(row=2, column=1, padx=5, pady=5)

        # Create a frame for the control fields
        control_frame = tk.Frame(self.root, bg=frame_bg)
        control_frame.pack(pady=10)
        
        # Create input fields for time delay and loop count
        tk.Label(control_frame, text="Time (s):", font=label_font, bg=frame_bg, fg="#dcdcdc").grid(row=0, column=0, padx=5)
        self.time_entry = tk.Entry(control_frame, width=10, bg=entry_bg, fg=entry_fg, borderwidth=entry_borderwidth, relief=entry_relief)
        self.time_entry.grid(row=0, column=1, padx=5)
        self.time_entry.insert(0, str(self.time_delay))

        tk.Label(control_frame, text="Loops (0=inf):", font=label_font, bg=frame_bg, fg="#dcdcdc").grid(row=0, column=2, padx=5)
        self.loop_entry = tk.Entry(control_frame, width=10, bg=entry_bg, fg=entry_fg, borderwidth=entry_borderwidth, relief=entry_relief)
        self.loop_entry.grid(row=0, column=3, padx=5)
        self.loop_entry.insert(0, str(self.loop_count))

        # Create a frame for the buttons
        button_frame = tk.Frame(self.root, bg=frame_bg)
        button_frame.pack(pady=20)

        # Create buttons for various actions
        tk.Button(button_frame, text="Add Function", command=self.add_function, bg=button_bg, fg=button_fg, font=label_font, relief="raised", bd=3).grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=5)
        tk.Button(button_frame, text="Remove Function", command=self.remove_function, bg=button_bg, fg=button_fg, font=label_font, relief="raised", bd=3).grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=5)
        tk.Button(button_frame, text="↑", command=self.move_up, bg=button_bg, fg=button_fg, font=label_font, relief="raised", bd=3).grid(row=1, column=0, padx=10, pady=10, ipadx=10, ipady=5)
        tk.Button(button_frame, text="↓", command=self.move_down, bg=button_bg, fg=button_fg, font=label_font, relief="raised", bd=3).grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=5)
        tk.Button(button_frame, text="Start", command=self.start_clicking, bg="#98c379", fg="#282c34", font=label_font, relief="raised", bd=3).grid(row=0, column=2, padx=10, pady=10, ipadx=10, ipady=5)
        tk.Button(button_frame, text="Stop", command=self.stop_clicking, bg="#e06c75", fg=button_fg, font=label_font, relief="raised", bd=3).grid(row=0, column=3, padx=10, pady=10, ipadx=10, ipady=5)

    # Method to update the mouse position label
    def update_mouse_position(self):
        try:
            # Get the current mouse position and pixel color
            x, y = pyautogui.position()
            color = pyautogui.pixel(x, y)
            # Update the label text
            self.mouse_position_label.config(text=f"Mouse Position: X={x}, Y={y}, Color={color}")
        except Exception:
            # Handle cases where the mouse position cannot be determined
            self.mouse_position_label.config(text="Mouse Position: N/A, Color=N/A")

        # Refresh the label every 100 ms
        self.root.after(100, self.update_mouse_position)

    # Method to set up global hotkeys
    def setup_global_shortcuts(self):
        """Sets up global hotkeys."""
        # Run the hotkey monitor in a separate thread
        threading.Thread(target=self.monitor_shortcuts, daemon=True).start()

    # Method to monitor for hotkey presses
    def monitor_shortcuts(self):
        """Monitors for global hotkey presses."""
        while True:
            # Stop the script if Ctrl+Q is pressed
            if keyboard.is_pressed("ctrl+q"):
                self.stop_script()
                break
            # Activate the color picker if Ctrl+P is pressed
            if keyboard.is_pressed("ctrl+p"):
                self.activate_color_picker()

    # Method to add a new click function
    def add_function(self):
        try:
            # Get values from the input fields
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            click_type = self.click_type_var.get()

            r = self.r_entry.get()
            g = self.g_entry.get()
            b = self.b_entry.get()

            # Check if a color is specified
            color = None
            if r and g and b:
                color = (int(r), int(g), int(b))

            # Add the new function to the list
            self.click_functions.append({"x": x, "y": y, "color": color, "click_type": click_type})
            # Refresh the listbox
            self.refresh_listbox()
        except ValueError:
            # Show an error message if the input is invalid
            messagebox.showerror("Error", "Please enter valid numerical values!")

    # Method to remove a selected function
    def remove_function(self):
        # Get the selected item from the listbox
        selected = self.listbox.curselection()
        if selected:
            # Remove the function from the list
            index = selected[0]
            self.click_functions.pop(index)
            # Refresh the listbox
            self.refresh_listbox()
        else:
            # Show a warning if no function is selected
            messagebox.showwarning("Warning", "No function selected to remove.")

    # Method to move a function up in the list
    def move_up(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            if index > 0:
                # Swap the function with the one above it
                self.click_functions[index], self.click_functions[index - 1] = (
                    self.click_functions[index - 1],
                    self.click_functions[index],
                )
                # Refresh the listbox
                self.refresh_listbox()
                # Keep the moved function selected
                self.listbox.select_set(index - 1)

    # Method to move a function down in the list
    def move_down(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            if index < len(self.click_functions) - 1:
                # Swap the function with the one below it
                self.click_functions[index], self.click_functions[index + 1] = (
                    self.click_functions[index + 1],
                    self.click_functions[index],
                )
                # Refresh the listbox
                self.refresh_listbox()
                # Keep the moved function selected
                self.listbox.select_set(index + 1)

    # Method to refresh the listbox
    def refresh_listbox(self):
        """Refreshes the listbox to display the current functions."""
        # Clear the listbox
        self.listbox.delete(0, tk.END)
        # Add each function to the listbox
        for func in self.click_functions:
            self.listbox.insert(tk.END, f"Type: {func['click_type']}, X={func['x']}, Y={func['y']}, Color={func['color']}")

    # Method to start the clicking process
    def start_clicking(self):
        try:
            # Get the time delay and loop count from the input fields
            self.time_delay = float(self.time_entry.get())
            self.loop_count = int(self.loop_entry.get())
            # Validate the time delay
            if self.time_delay <= 0:
                raise ValueError("Time must be a positive number.")
        except ValueError as e:
            # Show an error message if the input is invalid
            messagebox.showerror("Error", str(e))
            return

        # Start the clicking process in a new thread if it is not already running
        if not self.running:
            self.running = True
            threading.Thread(target=self.run_clicking).start()

    # Method to stop the clicking process
    def stop_clicking(self):
        self.running = False

    # Method that runs the clicking loop
    def run_clicking(self):
        loops_done = 0
        # Loop until the process is stopped
        while self.running:
            # Iterate through the list of functions
            for func in self.click_functions:
                # Stop if the process is no longer running
                if not self.running:
                    break

                # Get the function details
                x, y, color, click_type = func["x"], func["y"], func["color"], func["click_type"]

                action_taken = False
                # If a color is specified, check the pixel color before clicking
                if color:
                    # Ensure color is a tuple of integers
                    expected_color = tuple(map(int, color))
                    if pyautogui.pixel(x, y) == expected_color:
                        self.perform_click(x, y, click_type)
                        action_taken = True
                else:
                    # If no color is specified, click immediately
                    self.perform_click(x, y, click_type)
                    action_taken = True

                # If a click was performed, print a message and wait for the time delay
                if action_taken:
                    print(f"Action: {click_type} click at ({x}, {y})")
                    time.sleep(self.time_delay)

            # Check the loop count
            if self.loop_count > 0:
                loops_done += 1
                if loops_done >= self.loop_count:
                    self.running = False

            # Wait a short time before the next loop
            time.sleep(0.1)

    # Method to perform a click
    def perform_click(self, x, y, click_type):
        """Performs the specified click type at the given coordinates."""
        if click_type == "Left":
            pyautogui.click(x, y)
        elif click_type == "Right":
            pyautogui.rightClick(x, y)
        elif click_type == "Double":
            pyautogui.doubleClick(x, y)

    # Method to stop the script and close the application
    def stop_script(self, event=None):
        """Stops the script and closes the application."""
        self.stop_clicking()
        self.root.quit()

    # Method to activate the color picker
    def activate_color_picker(self, event=None):
        """Activates the color picker function."""
        try:
            # Get the current mouse position and color
            x, y = pyautogui.position()
            color = pyautogui.pixel(x, y)
            # Populate the input fields with the captured data
            self.x_entry.delete(0, tk.END)
            self.x_entry.insert(0, str(x))
            self.y_entry.delete(0, tk.END)
            self.y_entry.insert(0, str(y))
            self.r_entry.delete(0, tk.END)
            self.r_entry.insert(0, str(color[0]))
            self.g_entry.delete(0, tk.END)
            self.g_entry.insert(0, str(color[1]))
            self.b_entry.delete(0, tk.END)
            self.b_entry.insert(0, str(color[2]))
        except Exception as e:
            # Show an error message if the color cannot be captured
            messagebox.showerror("Error", f"Could not get color: {e}")

    # Method to save a profile
    def save_profile(self):
        """Saves the current click sequence to a JSON file."""
        # Open a file dialog to choose a save location
        filepath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="Save Profile"
        )
        if not filepath:
            return

        # Create a dictionary with the profile data
        profile_data = {
            "click_functions": self.click_functions,
            "time_delay": self.time_entry.get(),
            "loop_count": self.loop_entry.get()
        }

        # Save the data to a JSON file
        with open(filepath, "w") as f:
            json.dump(profile_data, f, indent=4)
        messagebox.showinfo("Success", "Profile saved successfully.")

    # Method to load a profile
    def load_profile(self):
        """Loads a click sequence from a JSON file."""
        # Open a file dialog to choose a file to load
        filepath = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            title="Load Profile"
        )
        if not filepath:
            return

        # Load the data from the JSON file
        with open(filepath, "r") as f:
            profile_data = json.load(f)

        # Update the application with the loaded data
        self.click_functions = profile_data.get("click_functions", [])
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, profile_data.get("time_delay", 1))
        self.loop_entry.delete(0, tk.END)
        self.loop_entry.insert(0, profile_data.get("loop_count", 0))
        self.refresh_listbox()
        messagebox.showinfo("Success", "Profile loaded successfully.")

    # Method to toggle the "Always on Top" state
    def toggle_always_on_top(self):
        self.root.attributes("-topmost", self.always_on_top_var.get())

# Main entry point of the application
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Create an instance of the application
    app = AutoClickerApp(root)
    # Start the GUI event loop
    root.mainloop()