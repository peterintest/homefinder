import pytest
from pytest_bdd import scenarios, given, when, parsers

pytestmark = pytest.mark.webtest

# Scenarios

scenarios('../features/users.feature')


# When Steps

@when('I select add user')
def select_add_user(browser, live_server):
    browser.links.find_by_partial_href(f'/auth/user/add/').click()


@when('I select change user')
def select_change_user(browser, live_server):
   browser.links.find_by_href('/admin/auth/user/').click()


@when('I select change password')
def select_change_password(browser, live_server):
   browser.links.find_by_href('../password/').click()


@when(parsers.parse('I add a user with the username "{username}"'))
def add_user(browser, live_server, username):
    browser.fill('username', username)
    browser.fill('password1', 'some_secure_password')
    browser.fill('password2', 'some_secure_password')


@when(parsers.parse('I update the user password to "{password}"'))
def update_user(browser, live_server, password):
    browser.fill('password1', password)
    browser.fill('password2', password)
