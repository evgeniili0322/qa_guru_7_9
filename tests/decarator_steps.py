import allure
from selene import browser, be, by


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
