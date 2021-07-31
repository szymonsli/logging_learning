# Logging learning in Python

*logging* - Module in the Python Standard Library. [Documentation](https://docs.python.org/3/library/logging.html)

## About
This short project is made to learn how logging in Python works. 
To run this project open the `logging_learning` directory in terminal and type:
```
$ python simple_calculator.py
```

If nothing was changed in `simple_calculator.py` script, you should see the following result:
```.env
INFO - simple_calculator::__init__  - The current number is 4
DEBUG - simple_calculator::add  - Added 2. The result is 6
DEBUG - simple_calculator::divide  - Divided by 3. The result is 2.0
DEBUG - simple_calculator::subtract  - Subtracted 1. The result is 1.0
DEBUG - simple_calculator::multiply  - Multiplied by 5. The result is 5.0
DEBUG - simple_calculator::divide  - Divided by 2. The result is 2.5
ERROR - simple_calculator::divide  - Tried to divide by 0. Skipped operation.
DEBUG - simple_calculator::add  - Added 13. The result is 15.5
```
Also, a new directory `logs` should be created with a `logger_0.log` file inside. 
Each time you run the script, a new log file is created.
