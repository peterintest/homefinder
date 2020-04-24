import pytest
from pytest_bdd import scenarios, given, when, parsers

pytestmark = pytest.mark.webtest

# Scenarios

scenarios('../features/services.feature')


# When Steps

@when('I select add service')
def select_add_service(browser, live_server):
    browser.links.find_by_partial_href(f'/service/add/').click()


@when('I select change service')
def select_change_service(browser, live_server):
   browser.links.find_by_href('/admin/services/service/').click()


@when(parsers.parse('I add a service with the name "{name}"'))
def add_service(browser, live_server, name):
    browser.fill('name', name)


@when(parsers.parse('I update the service name to "{name}"'))
def update_service(browser, live_server, name):
    browser.fill('name', name)
