import pytest
from pytest_bdd import scenarios, given, when, parsers

pytestmark = pytest.mark.webtest

# Scenarios

scenarios('../features/customers.feature')


# When Steps

@when('I select add customer')
def select_add_customer(browser, live_server):
    browser.links.find_by_partial_href(f'/customer/add/').click()


@when('I select change customer')
def select_change_customer(browser, live_server):
   browser.links.find_by_href('/admin/customers/customer/').click()


@when(parsers.parse('I add a customer with the name "{name}"'))
def add_customer(browser, live_server, name):
    browser.fill('name', name)
    browser.fill('address', 'Hills Road')
    browser.fill('city', 'Cambridge')
    browser.fill('county', 'Cambridgeshire')
    browser.fill('postcode', 'CB2')
    browser.fill('email', 'customer@test.com')
    browser.fill('phone', '012345678901')


@when(parsers.parse('I update the customer email to "{email}"'))
def update_customer(browser, live_server, email):
    browser.fill('email', email)
