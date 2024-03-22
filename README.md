# Django With Tailwind CSS

A demo using tailwind css in Django, referenced in this [article](https://www.photondesigner.com/articles/tailwind-with-django).

## Install Tailwind CSS

1. Download the [Tailwind CSS Standalone CLI](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.4.1)
2. Rename
   ```bash
   mv tailwindcss-xxx-xxx tailwindcss
   ```
3. Make it executable
   ```bash
   chmod +x tailwindcss
   ```

## Start the Tailwind watcher

1. Create `tailwind_watcher.py` in your **core** directory
   ```python
   import subprocess


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
       # will be printed twice because Django will automatically restart once. (Explanation given by GPT)
       print('TailwindCSS watcher started.')
   ```


2. Add the following code to the end of the settings.py file
   ```python
   from . import tailwind_watcher

   # run the watcher in development (given reasons mentioned in the guide).
   if DEBUG:
       tailwind_watcher.run_tailwind_watch()
   ```


## Run

```bash
> python manage.py runserver 0.0.0.0:8080
TailwindCSS watcher started.
TailwindCSS watcher started.

Rebuilding...
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 22, 2024 - 11:31:05
Django version 5.0.3, using settings 'core.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
```

Then you will find the `output.css` file in the `sim/static/css directory`.