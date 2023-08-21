from decarator_steps import *


def test_check_issue_name(browser_opt):
    browser.open('')

    # Act
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    # Assert
    browser.element('.js-navigation-container').element(by.partial_text('#76')).should(be.visible)


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


def test_check_issue_name_decorator_steps(browser_opt):
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    got_to_repository('eroshenkoam/allure-example')
    open_issues_tab()
    issue_should_be_visible(76)
