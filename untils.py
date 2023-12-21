import threading
import keyboard

def perform_until_z(operation:callable):
    # Shared flag to control both threads
    stop_flag = threading.Event()

    # Function to check for 'z' key press and set the stop flag
    def check_for_z_key():
        while not stop_flag.is_set():
            if keyboard.is_pressed('z'):
                stop_flag.set()

    # Function to simulate a mouse click every second
    def simulate_mouse_click():
        try:
            while not stop_flag.is_set():
                operation()
        except KeyboardInterrupt:
            pass

    # Create two threads for the operations
    thread1 = threading.Thread(target=check_for_z_key)
    thread2 = threading.Thread(target=simulate_mouse_click)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the 'Z' key thread to finish
    thread1.join()

    # Set the stop flag to stop the mouse clicking thread
    stop_flag.set()

    # Wait for the mouse clicking thread to finish
    thread2.join()
