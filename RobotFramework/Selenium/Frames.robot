'''
A frame or iframe is an HTML document embedded inside another HTML page.

frames will have ids

framses will have name

frames  will class

with indexes

0 or 1

'''

*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://jqueryui.com/datepicker/

*** Test Cases ***
Verify multiple window handling
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    3s
    Select Frame    //iframe[@class='demo-frame']
    Sleep    5s
    Click Element    //input[@id='datepicker']
    Sleep    5s
    Click Element    //a[contains(text(),'21')]
    Sleep    5s
    Unselect Frame
    Close Browser