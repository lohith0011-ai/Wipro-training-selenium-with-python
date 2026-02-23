*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://www.amazon.in/

*** Test Cases ***
Verify scroll to footer
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    //a[normalize-space()='Sell on Amazon']    timeout=15s
    Scroll Element Into View         //a[normalize-space()='Sell on Amazon']

    Sleep    3s
    Click Element    //a[normalize-space()='Sell on Amazon']
    sleep       5s
    Close Browser