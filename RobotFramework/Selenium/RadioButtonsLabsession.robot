*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/check-box.php


*** Test Cases ***
Verify radio buttons
        Open Browser        ${url}       chrome
        # maximize the browser window
        Maximize Browser Window
        # wait till the element is loaded
        Wait Until Element Is Visible    xpath://input[@id='c_bs_1']
        # click on check box
        Click Element    xpath://input[@id='c_bs_1']
        # wait till the element is loaded
        Wait Until Element Is Visible    xpath://input[@id='c_bs_2']
        # click on check box
        Click Element    xpath://input[@id='c_bs_2']
        # close browser
        Sleep    10s
        Close Browser