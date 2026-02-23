*** Settings ***
Library    Collections

*** Variables ***
${NAME}       Lohith
${CITY}       Hyderabad
@{FRUITS}     Apple    Mango    Banana
&{USER}       name=Lohith    age=22    city=Hyderabad

*** Test Cases ***

1. Scalar Variable
    Log    ${NAME}

2. Sum Of Two Numbers
    ${a}=    Set Variable    10
    ${b}=    Set Variable    20
    ${sum}=  Evaluate    ${a}+${b}
    Log    Sum is ${sum}

3. Variable Inside Sentence
    Log    I live in ${CITY}

4. Reassign Variable
    ${NAME}=    Set Variable    Kumar
    Log    Updated name is ${NAME}

5. List Variable First Item
    Log    ${FRUITS}[0]

6. Loop Through List
    FOR    ${item}    IN    @{FRUITS}
        Log    ${item}
    END

7. Length Of List
    ${length}=    Get Length    ${FRUITS}
    Log    Length is ${length}

8. Dictionary Key Value
    Log    ${USER}[name]

9. Add Key Value To Dictionary
    Set To Dictionary    ${USER}    country=India
    Log    ${USER}

10. Loop Dictionary
    FOR    ${key}    ${value}    IN    &{USER}
        Log    ${key} = ${value}
    END