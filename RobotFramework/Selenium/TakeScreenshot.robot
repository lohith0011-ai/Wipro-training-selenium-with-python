*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}      https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify radio buttons
        Open Browser       ${url}        chrome
        # maximize the browser window
        Maximize Browser Window
        # wait till the element is loaded
        Sleep    3s
        Wait Until Element Is Visible    xpath://input[@id='file-upload']
        # capture page screenshot
        Capture Page Screenshot     C://Pictures//Picture1.jpg
        # capture element screenshot
        Capture Element Screenshot    xpath://input[@id='file-upload']       C://Pictures//Picture2.jpg
        Sleep    3s
        # close browser
        Close Browser