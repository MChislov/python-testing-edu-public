*** Settings ***
Library           SeleniumLibrary
Variables         ../PagesLocators/cartPageLocators.py

*** Keywords ***
Wait Until Cart Page Is Loaded
    [Arguments]    ${timeout}
    SeleniumLibrary.Wait Until Element Is Visible    ${PlaceOrderLink}    timeout=${timeout}

Check Product Is In The Cart
    [Arguments]    ${product_title}    ${product_price}
    SeleniumLibrary.Wait Until Element Is Visible    //*[@class='table-responsive']//tr[@class='success']/td[text()='${product_title}']    timeout=1s
    SeleniumLibrary.Wait Until Element Is Visible    //*[@class='table-responsive']//tr[@class='success']/td[text()='${product_price}']    timeout=1s
