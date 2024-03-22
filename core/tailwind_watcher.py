import subprocess
# import threading


def run_tailwind_watch():
    """
    Runs TailwindCSS in watch mode for automatic recompilation.
    """
    command = [
        # Make sure that this points to your tailwindcss file in your project.
        './tailwindcss',
        '-i', './sim/static/css/input.css',  # input
        '-o', './sim/static/css/output.css',  # output
        '--watch'
    ]
    # Using subprocess.Popen instead of subprocess.run to not block the thread waiting for the process to complete.
    subprocess.Popen(command, stdout=subprocess.DEVNULL)
    # Dont wait for the command to complete
    # process.communicate()
    # will be printed twice because Django will automatically restart once.
    print('TailwindCSS watcher started.')


# def start():
#     """
#     Starts the TailwindCSS watcher in a separate thread.
#     """
#     thread = threading.Thread(target=run_tailwind_watch)
#     thread.start()


# if __name__ == "__main__":
#     run_tailwind_watch()
