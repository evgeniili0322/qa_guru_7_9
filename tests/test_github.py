import allure
from allure_commons.types import Severity
from selene import browser, be, by


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Issues')
@allure.story('Find issue #80 in repository')
@allure.link('https://github.com')
def test_check_issue_name(browser_opt):
    browser.open('')

    # Act
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    # Assert
    browser.element('.js-navigation-container').element(by.partial_text('#80')).should(be.visible)


@allure.tag('Web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Issues')
@allure.story('Find issue #76 in repository')
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

    with allure.step('Check if issue with #76 visible'):
        browser.element('.js-navigation-container').element(by.partial_text('#76')).should(be.visible)


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Issues')
@allure.story('Find issue #78 in repository')
@allure.link('https://github.com')
def test_check_issue_name_decorator_steps(browser_opt):
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    got_to_repository('eroshenkoam/allure-example')
    open_issues_tab()
    issue_should_be_visible(78)


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


@allure.step('Check if issue with #{issue_number} visible')
def issue_should_be_visible(issue_number):
    browser.element('.js-navigation-container').element(by.partial_text(f'#{issue_number}')).should(be.visible)
