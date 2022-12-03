*** Settings ***
Library           SeleniumLibrary
Variables         ../PagesLocators/monitorsPageLocators.py

*** Keywords ***
Wait Until First Product Card Is Visible
    [Arguments]    ${timeout}
    Wait Until Element Is Visible    ${FirstProductCard}    timeout=${timeout}
