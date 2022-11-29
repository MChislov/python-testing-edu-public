*** Settings ***
Resource          PageObject/KeywordDefinitionFiles/loginPage.resource
Resource          PageObject/KeywordDefinitionFiles/mainPage.resource
Resource          PageObject/KeywordDefinitionFiles/monitorsPage.resource
Resource          PageObject/KeywordDefinitionFiles/cartPageResource.resource
Library           ../findMaxPriceProduct.py    WITH NAME    MaxPriceProductDetails
Library           String

*** Variables ***
${base_url}       https://www.demoblaze.com

*** Keywords ***
Click Link Custom
    [Arguments]    ${link_text}
    [Tags]    screenshot
    SeleniumLibrary.Wait Until Element Is Visible    //*[text()='${link_text}']    timeout=5s
    SeleniumLibrary.Click Element    //*[text()='${link_text}']

Close Alert Dialog
    SeleniumLibrary.Press Keys    None    RETURN
