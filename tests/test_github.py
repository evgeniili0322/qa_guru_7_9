import allure
from allure_commons.types import Severity
from selene import browser, by, have


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Issues')
@allure.story('Issue #80 in repository should have name "e.sh"')
@allure.link('https://github.com')
def test_check_issue_name(browser_opt):
    browser.open('')

    # Act
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    # Assert
    browser.element('#issue_80').should(have.text('e.sh'))


@allure.tag('Web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Issues')
@allure.story('Issue #76 in repository should have name "С Новым Годом (2022)"')
@allure.link('https://github.com')
def test_check_issue_name_dynamic_steps(browser_opt):
    with allure.step('Open main page'):
        browser.open('')

    with allure.step('Search repository'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Go to repository'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open "Issues" tab'):
        browser.element('#issues-tab').click()

    with allure.step('Check issue with #76 have name "С Новым Годом (2022)"'):
        browser.element('#issue_76').should(have.text('С Новым Годом (2022)'))


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Issues')
@allure.story('Issue #68 in repository should have name "Listeners NamedBy"')
@allure.link('https://github.com')
def test_check_issue_name_decorator_steps(browser_opt):
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    got_to_repository('eroshenkoam/allure-example')
    open_issues_tab()
    issue_should_have_name(68)


@allure.step('Open main page')
def open_main_page():
    browser.open('')


@allure.step('Search repository {repo}')
def search_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step('Go to repository {repo}')
def got_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Open "Issues" tab')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Check issue with #{issue_number} have name "Listeners NamedBy"')
def issue_should_have_name(issue_number):
    browser.element(f'#issue_{issue_number}').should(have.text('Listeners NamedBy'))
