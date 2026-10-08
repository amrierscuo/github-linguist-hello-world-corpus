*** Settings ***
Resource    hello.resource
*** Test Cases ***
Greeting value
    ${message}=    Greeting
    Should Be Equal    ${message}    Hello, World!
    Log To Console    ${message}
