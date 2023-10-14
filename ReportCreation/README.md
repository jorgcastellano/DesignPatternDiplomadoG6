# darqs_design_patterns_g6
***
This application represents the implementation of the Strategy design pattern, this is represented by the problem of generating reports in different formats (PDF, EXCEL and HTML).

Pattern Type: 
Behavioral

Design Pattern
Strategy: behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

## Requirements
Requirements for running the application
```bash
Python 3.6+
```

## Installation
A little intro about the installation. 
```
$ git clone https://github.com/jorgcastellano/darqs_design_patterns_g6.git
$ cd ../path/to/the/file
```

## Use
```
$ python main.py
```

Objects that can be sent in main.py
* reportresult = report.generate(ReportPDF())
* reportresult = report.generate(ReportHTML())
* reportresult = report.generate(ReportExcel())


## Contribution
If you wish to contribute to this project, follow these guidelines:

* Create a fork of the repository.
* Clone your fork: git clone https://github.com/jorgcastellano/darqs_design_patterns_g6.git
* Create a branch for your changes: git checkout -b new-feature
* Make your modifications and commit: git commit -m "Add new feature"
* Push your changes to your fork: git push origin new-feature
* Create a pull request on the original repository.

## Class Diagram

<img width="916" alt="Screenshot 2023-10-12 at 11 10 59 PM" src="https://github.com/jorgcastellano/darqs_design_patterns_g6/assets/52435269/3b8c90bc-a13f-43d3-bece-058e9a2a660c">
