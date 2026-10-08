*** Variables ***
${NAME}    World

*** Test Cases ***
Original greeting
    ${message}=    Set Variable    Hello, ${NAME}!
    Should Be Equal    ${message}    Hello, World!
    Log To Console    ${message}
