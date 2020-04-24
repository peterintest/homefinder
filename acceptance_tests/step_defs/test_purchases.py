import pytest
from pytest_bdd import scenarios, given, when, parsers

# Scenarios

scenarios('../features/purchases.feature')

pytestmark = pytest.mark.webtest

# When Steps

@when('I select add purchase')
def select_add_purchase(browser, live_server):
    browser.links.find_by_partial_href(f'/purchase/add/').click()


@when('I select change purchase')
def select_change_purchase(browser, live_server):
    browser.links.find_by_partial_href('/admin/sales/purchase/').click()


@when(parsers.parse('I add a purchase for the listing "{listing_title}"'))
def add_purchase(browser, live_server, listing_title):
    browser.find_by_id('id_customer').select(1)
    browser.find_by_id('id_listing').select_by_text(listing_title)
    browser.find_by_id('id_agent').select(1)
    browser.fill('amount', 350000)


@when(parsers.parse('I update the purchase price to "{price}"'))
def update_purchase(browser, live_server, price):
    browser.fill('amount', price)
