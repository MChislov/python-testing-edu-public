*** Settings ***
Library           SeleniumLibrary
resource    KeywordResources/common.resource

*** Variables ***
${base_url}       https://www.demoblaze.com
${registered_username}    mc1
${registered_password}    mc1pass

*** Test Cases ***
TC_01
    Login With Registered User
    SeleniumLibrary.Wait Until Page Contains Element    //*[text()='Log out']    timeout=1s
    [Teardown]    SeleniumLibrary.Close Browser

TC_02
    Login With Registered User
    Click Link    Monitors
    Sleep    5s
    ${max_price_item_index}    ${max_price}    ${product_title}    Get Max Price Item Index Price Name
    SeleniumLibrary.Click Element    //*[@class='card h-100']/../../div[${max_price_item_index}]
    Click Link    Add to cart
    SeleniumLibrary.Press Keys    None    RETURN
    Click Link    Cart
    SeleniumLibrary.Wait Until Element Is Visible    //*[text()='Place Order']    timeout=5s
    SeleniumLibrary.Wait Until Element Is Visible    //*[@class='table-responsive']//tr[@class='success']/td[text()='${product_title}']    timeout=1s
    SeleniumLibrary.Wait Until Element Is Visible    //*[@class='table-responsive']//tr[@class='success']/td[text()='${max_price}']    timeout=1s
    [Teardown]    SeleniumLibrary.Close Browser

*** Keywords ***
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

Click Link
    [Arguments]    ${link_text}
    [Tags]    screenshot
    SeleniumLibrary.Wait Until Element Is Visible    //*[text()='${link_text}']    timeout=5s
    SeleniumLibrary.Click Element    //*[text()='${link_text}']

Get Max Price Item Index Price Name
    [Tags]    screenshot
    ${count}    SeleniumLibrary.Get Element Count    //div[@class='card h-100']//*[@class='card-block']/h5
    ${max_price}    Set Variable    0
    ${max_price_item_index}    Set Variable    0
    FOR    ${index}    IN RANGE    1    ${count}+1
        SeleniumLibrary.Wait Until Element Is Visible    //*[@class='card h-100']/../../div[${index}]//h5
        ${price}    SeleniumLibrary.Get Text    //*[@class='card h-100']/../../div[${index}]//h5
        ${current_price}    Convert To Integer    ${price}[1:]
        ${max_price}    Set Variable If    ${current_price}>${max_price}    ${current_price}    ${max_price}
        ${max_price_item_index}    Set Variable If    ${current_price}==${max_price}    ${index}    ${max_price_item_index}
    END
    ${product_title}    SeleniumLibrary.Get Text    //*[@class='card h-100']/../../div[${max_price_item_index}]//h4[@class='card-title']/a
    [Return]    ${max_price_item_index}    ${max_price}    ${product_title}
