# Lab 5 – Reflection

## 1. What did you learn from static code analysis?

I learned that static code analysis helps identify code quality, formatting, programming mistakes, and security vulnerabilities without executing the program. Pylint, Bandit, and Flake8 helped me identify different categories of problems.

## 2. Which tool was most useful and why?

Bandit was particularly useful because it identified security vulnerabilities such as unsafe eval(), weak MD5 hashing, insecure OTP generation, hardcoded secrets, and unsafe shell command execution.

## 3. What was the most important issue you fixed?

Replacing eval() was one of the most important fixes because evaluating expressions can allow unsafe code execution. I replaced it with a safer numeric discount calculation. I also replaced MD5 with SHA-256 and used the secrets module for OTP generation.

## 4. How did you verify that your fixes worked?

I reran Python compilation and execution, Pylint, Bandit, and Flake8 after making the changes. The final results were:
- Pylint: 9.84/10
- Bandit: Zero security issues identified.
- Flake8: Zero violations.
- Python compilation: Successful.
- Program execution: Successful.
