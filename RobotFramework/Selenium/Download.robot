*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}              https://the-internet.herokuapp.com/download
*** Test Cases ***
Verify File Downloads

        Open Browser        ${url}      chrome
        #maximize the window
        Maximize Browser Window
        Wait Until Element Is Visible       xpath://a[normalize-space()='upload.txt']

        Click Element    xpath://a[normalize-space()='upload.txt']

        Sleep    5s


        #close browser
        Close Browser