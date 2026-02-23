*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}             https://www.tutorialspoint.com/selenium/practice/frames.php

*** Test Cases ***
Verify Frames

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Set Selenium Implicit Wait    3s
        Select Frame    xpath://body//main//iframe[1]
        Get WebElements    xpath://h1[normalize-space()='Selenium - Automation Practice Form']
        Sleep    2s
        Unselect Frame
        Select Frame    xpath://body//main//iframe[2]
        Get WebElements    xpath://a[normalize-space()='']//*[name()='svg']//*[name()='path']
        Sleep    2s
        Unselect Frame
        #close browser
        Close Browser