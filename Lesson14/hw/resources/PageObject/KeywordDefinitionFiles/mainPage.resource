*** Settings ***
Library           SeleniumLibrary
Variables         ../PagesLocators/mainPageLocators.py

*** Keywords ***
Open Login Dialog
    [Arguments]    ${base_url}    ${browser}=chrome
    SeleniumLibrary.Open Browser    ${base_url}    browser=${browser}
    SeleniumLibrary.Maximize Browser Window
    SeleniumLibrary.Wait Until Element Is Visible    ${ButtonLogin}    timeout=5s
    SeleniumLibrary.Click Element    ${ButtonLogin}
