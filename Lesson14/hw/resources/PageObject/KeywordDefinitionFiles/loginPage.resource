***Variables***
${registered_username}    mc1
${registered_password}    mc1pass

***Keywords***
Login With Registered User
    [Tags]    screenshot
    SeleniumLibrary.Open Browser    ${base_url}    browser=chrome
    SeleniumLibrary.Maximize Browser Window
    SeleniumLibrary.Wait Until Element Is Visible    login2    timeout=5s
    SeleniumLibrary.Click Element    login2
    SeleniumLibrary.Wait Until Element Is Visible    loginusername    timeout=5s
    SeleniumLibrary.Input Text    loginusername    ${registered_username}
    SeleniumLibrary.Input Text    loginpassword    ${registered_password}
    SeleniumLibrary.Click Button    //button[text()='Log in']
    SeleniumLibrary.Wait Until Page Contains Element    //*[text()='Welcome ${registered_username}']    timeout=5s