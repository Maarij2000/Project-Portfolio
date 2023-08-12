Personal Projects
- Real Estate Website using HTML and CSS
- AI Voicebot using Python and IBM Watson
- AI Research on Human-Robot Coexistance
- Predict cause of UAE traffic accidents using 2021 UAE accidents dataset and accident size in UAE using 2013-2019 UAE accidents dataset while taking other factors into account like weather condition, road condition and so on.
- Data Lake implementation for FortyGuard, which is a company that provides outdoor weather data analysis services
- 
- QueryCure
This project is a C++ application that integrates with an Oracle database using the sqlAPI++ library. It includes a graphical user interface built using the wxWidgets library.

Project Scope & Objectives
Query Cure is a database diagnosis tool which is made using C++. It can be installed on any client/server where the diagnosis is run. The tool will gain insights based on the database and display suggestions on how to improve the performance such as denormalization, indexing, clustering, etc. It involves the following components:

Data Collection
It can collect performance metrics and data from the Oracle database server. This data can include information on CPU utilization, memory usage, disk I/O, and other database-related statistics.

Data Analysis
It can analyze the data collected and identify any performance issues or bottlenecks in the database. This can involve identifying slow-running queries, inefficient indexing, or other performance-related issues.

Recommendations
Once the tool has identified performance issues, it should provide recommendations for improving the performance of the database. This can include suggestions for tuning the database configuration, optimizing SQL queries, or adding or modifying database indexes.

Reporting
The tool should be able to generate reports that summarize the performance of the database, including any issues that were identified and any recommendations for improvement.

Monitoring
It monitors the performance of the database over time and provides alerts if performance issues occur. This can include monitoring the database for spikes in resource utilization or other anomalies that could indicate a performance problem.

Methodology and Technology used
Microsoft Visual Studio Community Edition
Used as the IDE and debugger for the project.

C++
Used for the logic implementation and connection to SQL databases.

wxWidgets (C++ GUI)
Used as a C++ library to implement a graphical interface.

sqlAPI++
C++ library that allows PL/SQL statements to be run from C++ functions.

Oracle Express Edition 21c Database and Oracle Instant Client
Used to test the application and interact with Oracle databases.

Windows 10/11
Used to develop and test the application.

Installation
Install Oracle Express Edition, Oracle Install Client and set up a database..
Install wxWidgets 3.1.5 or later on your system.
Install SQLAPI++.
Clone this repository to your local machine git clone https://github.com/IbrahimSiddiqui007/QueryCure.git.
Open the solution file *.sln in Visual Studio 2022.
Build the project.
Run the application.
