*** Settings ***
Library           SeleniumLibrary
Variables         ../PagesLocators/loginPageLocators.py

*** Variables ***

*** Keywords ***
Login With Registered User
    [Tags]    screenshot
    SeleniumLibrary.Wait Until Element Is Visible    ${LoginField}    timeout=5s
    SeleniumLibrary.Input Text    ${LoginField}    ${ValidUsername}
    SeleniumLibrary.Input Text    ${PasswordField}    ${ValidPassword}
    SeleniumLibrary.Click Button    ${SubmitLoginButton}
    SeleniumLibrary.Wait Until Page Contains Element    //*[text()='Welcome ${ValidUsername}']    timeout=5s
