import os
import subprocess

# Define the name of the virtual environment
venv_name = "myenv"

# Create a virtual environment
subprocess.run(["python", "-m", "venv", venv_name], check=True)

# Activate the virtual environment (for Windows)
if os.name == "nt":
    activate_script = os.path.join(venv_name, "Scripts", "activate")
    activate_cmd = f"{activate_script} &&"
else:
    activate_cmd = f"source {venv_name}/bin/activate &&"

# Install libraries from requirements.txt
requirements_file = "requirements.txt"
install_command = f"{activate_cmd} pip install -r {requirements_file}"
subprocess.run(install_command, shell=True, check=True)

print(f"Virtual environment '{venv_name}' created and libraries installed.")

# Run another Python file (replace 'your_script.py' with the actual filename)
subprocess.run([f"{activate_cmd} python your_script.py"], shell=True, check=True)
