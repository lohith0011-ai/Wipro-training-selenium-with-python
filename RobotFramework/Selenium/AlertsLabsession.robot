*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.tutorialspoint.com/selenium/practice/alerts.php


*** Test Cases ***
Verify drop downs
        Open Browser        ${url}        chrome
        # maximize the browser window
        Maximize Browser Window
        Wait Until Element Is Visible    xpath=(//button)[6]
        Click Element    xpath:(//button)[6]
        # Information alert - accept is for ok button
        Handle Alert      action=ACCEPT        timeout=3
        Sleep    5s
        Click Element    xpath:(//button)[8]
        # Confirmational alert - accept is for ok button dismiss is for cancel button
        Handle Alert      action=DISMISS       timeout=3
        Sleep    5s
        # Prompt alert - accept is for ok button dismiss is for cancel button
        Click Element    xpath:(//button)[9]
        Input Text Into Alert    Hello
        Sleep    5s
        Close Browser