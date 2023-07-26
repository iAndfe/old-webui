import subprocess
import time

def run_application():
    while True:
        print("Starting the application...")
        process = subprocess.Popen(['./webui.sh'])

        # Wait for the application to finish running
        exit_code = process.wait()

        # If the application exited normally, break the loop
        if exit_code == 0:
            break

        print("Application stopped with exit code", exit_code)
        print("Restarting the application after 1 second...")
        time.sleep(1)

# Call the function to start your application
run_application()