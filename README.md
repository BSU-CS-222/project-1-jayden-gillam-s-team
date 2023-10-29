[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/qOno1FyB)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12187192&assignment_repo_type=AssignmentRepo)
# Project 1

Joshua Williams and Jayden Gillam
Live Internet JSON Data Retrieval and Display

ENTRY POINTS:

- Console Based Application - project1.py

- GUI Application - project1GUI.py

This Python program provides a simple way to retrieve and display information from a Wikipedia page using the Wikipedia API. The program includes two main functions:

1.) get_json_dict(condensed_page_name: str) -> dict:

-This function takes a single argument, condensed_page_name, which is a string representing the title of the Wikipedia page you want to retrieve information for.

-It constructs a URL to the Wikipedia API and fetches the JSON data for the specified page.

-The JSON data is then parsed into a Python dictionary and returned.

2.) display_information(json_dict: dict) -> None:

-This function takes a JSON dictionary, json_dict, as input, which is the data returned from the Wikipedia API using the get_json_dict function.

-It extracts and displays information about the specified Wikipedia page, including any redirects and details of the revisions made to the page.

if __name__ == "__main__":

This section is used to run the program when the script is executed as the main module. However, there's a reference to a main() function that is missing in the provided code. To make the script work, you should define a main() function and call it within this block. The main() function should call the get_json_dict and display_information functions to retrieve and display the Wikipedia page information.

Project1 Test Suite

This is a test file designed to test the functions and methods in the "project1" module using the Python unittest framework. The test suite includes two test cases:

1.) test_condensePageName:

-This test case verifies the functionality of the condense_page_name function.

-It checks whether the function correctly condenses a page name, removing extra spaces and converting it into a format suitable for a Wikipedia page title.

-It uses the assertEqual method to compare the output of the condense_page_name function with the expected result.

2.) test_getJsonDict:

-This test case checks the functionality of the get_json_dict function.

-It tests whether the function can successfully fetch and parse JSON data from the Wikipedia API for a specified page.

-It uses the assertEqual method to verify that the returned data is of type dict.

Usage

To run the tests defined in this file, you can execute it as the main module. When executed, it will use the unittest framework to run the defined test cases. If the functions being tested are correctly implemented, the test cases will pass without any assertion errors. If there are issues with the functions, the test cases will highlight them.

In the if __name__ == "__main__": block, the unittest.main() function is called to discover and run the tests. To use this test suite, ensure that your "project1" module is correctly imported and contains the functions condense_page_name and get_json_dict. If you have additional functions to test, you can define more test cases within this test file.

Iteration 2 GUI

This Python program is a Graphical User Interface (GUI) application that allows users to query and retrieve information about Wikipedia page revisions. The GUI is built using the Tkinter library and provides a user-friendly interface to interact with the Wikipedia API. Here's a brief description of the GUI and its features:

Features:

1.) Search Input: Users can enter the title of the Wikipedia page they want to query into the text entry field. The program handles input validation and formatting to ensure proper query execution.

2.) Query Button: Clicking the "Query" button initiates the query process. The program will send a request to the Wikipedia API to fetch information about the specified page.

3.) Revisions List: The retrieved information is displayed in the listbox, allowing users to view details about the page, including revisions and redirects.

How to Use:

1.) Launch the application by running the script.

2.) Enter the title of the Wikipedia page you want to query into the text entry field.

3.) Click the "Query" button to fetch information.

4.) The listbox will display the results, which may include revisions, redirects, or error messages if the article is not found or if there is a network issue.

Dependencies:

The program relies on several Python modules, including json, ssl, urllib.request, and tkinter. Ensure that these modules are properly installed on your system.

Important Note:

-Make sure to import the necessary modules and ensure that the functions get_json_dict, add_information, and condense_page_name are correctly defined in your "project1" module for the GUI to work properly. The GUI interacts with these functions to retrieve and display Wikipedia page information.

-The GUI provides a user-friendly way to utilize the functionality of the "project1" module for querying Wikipedia page revisions.

-Customize and extend the GUI as needed to meet the specific requirements of your project. You can add additional features, error handling, and improvements to enhance the user experience.