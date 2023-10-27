# Assignment-Nelkinda
Check if Python is Installed:
Ensure that Python is installed on system. Check this by running the following command in the terminal or command prompt:

python --version

Verify Python Installation:
After installing or reinstalling Python, make sure to verify that pip is available. 
Run the following command to check if pip is installed:

python -m ensurepip --default-pip

After making these changes, verify that pip is now accessible by running:

pip --version

To automatically run tests whenever make changes to the code,use tools like pytest-watch. 

Install it using pip:

pip install pytest-watch

Then, run pytest-watch to continuously monitor the code and run the tests automatically when changes are detected:

ptw

run the bat file which will run the test cases automatically

./run_tests.bat
