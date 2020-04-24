import pytest
from pytest_bdd import scenarios, given, when, parsers

pytestmark = pytest.mark.webtest

# Scenarios

scenarios('../features/sales.feature')


# When Steps

@when('I select add sale')
def select_add_sale(browser, live_server):
    browser.links.find_by_partial_href(f'/sale/add/').click()


@when('I select change sale')
def select_change_sale(browser, live_server):
    browser.links.find_by_partial_href('/admin/sales/sale/').click()


@when(parsers.parse('I add a sale for the listing "{listing_title}"'))
def add_sale(browser, live_server, listing_title):
    browser.find_by_id('id_customer').select(1)
    browser.find_by_id('id_listing').select_by_text(listing_title)
    browser.find_by_id('id_agent').select(1)
    browser.fill('amount', 350000)


@when(parsers.parse('I update the sale price to "{price}"'))
def update_sale(browser, live_server, price):
    browser.fill('amount', price)
