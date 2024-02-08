1. Install a virtual environment
    > py -m pip install virtualenv

2. Create the virtual environment
    > py -m venv venv_ui_test

3. Got to the virtual environment dir
    > cd venv_ui_test

4. Run the virtual environment
    > Script\activate

5. Copy sent files to 'venv_ui_test' dir

6. Install necessary packages
   > py -m pip install -r requirements.txt
 
7. Run tests
   > behave tests/e2e/features/ 
   