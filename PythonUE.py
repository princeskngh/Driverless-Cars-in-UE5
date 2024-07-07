import subprocess

try:
    # Launch the server.exe file
    server_path = r"D:\Downloads D\UEPython_tutorial_2-main\UEPython_tutorial_2-main\Python\dist\server\server.exe"
    subprocess.Popen(server_path)
except FileNotFoundError as e:
    print(f"File not found: {e.filename}")
except Exception as e:
    print(f"An error occurred: {str(e)}")