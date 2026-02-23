*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections

*** Variables ***
${url}      https://www.amazon.in/

*** Test Cases ***
Get all links from Amazon
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Set Selenium Implicit Wait    5s

    @{links}=    Get All Links
    ${count}=    Get Length    ${links}

    Log To Console    Total links found: ${count}
    Log To Console    First 10 links:
    FOR    ${link}    IN    @{links}[0:10]
        Log To Console    ${link}
    END

    Close Browser