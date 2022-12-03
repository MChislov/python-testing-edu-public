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
