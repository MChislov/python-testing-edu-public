*** Settings ***
Resource          resources/common.resource

*** Variables ***

*** Test Cases ***
TC_01
    [Setup]    Open Login Dialog    ${base_url}
    Login With Registered User
    SeleniumLibrary.Wait Until Page Contains Element    //*[text()='Log out']    timeout=1s
    [Teardown]    SeleniumLibrary.Close Browser

TC_02
    [Setup]    Open Login Dialog    ${base_url}
    Login With Registered User
    Click Link Custom    Monitors
    Sleep    3s
    Wait Until First Product Card Is Visible    5s
    ${max_price_item_index}    ${max_price}    ${product_title}    MaxPriceProductDetails.Get Max Price Card Details
    SeleniumLibrary.Click Element    //*[@class='card h-100']/../../div[${max_price_item_index}]
    Click Link Custom    Add to cart
    Close Alert Dialog
    Click Link Custom    Cart
    Wait Until Cart Page Is Loaded    5s
    Check Product Is In The Cart    ${product_title}    ${max_price}
    [Teardown]    SeleniumLibrary.Close Browser

*** Keywords ***
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
