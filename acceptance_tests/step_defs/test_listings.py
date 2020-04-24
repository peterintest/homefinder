import os
import pytest
from pytest_bdd import scenarios, given, when, parsers

pytestmark = pytest.mark.webtest

# Scenarios

scenarios('../features/listings.feature')


# When Steps

@when('I select add listing')
def select_add_listing(browser, live_server):
    browser.links.find_by_partial_href(f'/listing/add/').click()


@when('I select change listing')
def select_change_listing(browser, live_server):
   browser.links.find_by_partial_href('/admin/listings/listing/').click()


@when(parsers.parse('I uncheck is published'))
def uncheck_is_published(browser, live_server):
    browser.uncheck('is_published')


@when(parsers.parse('I add a listing with the title "{title}"'))
def add_listing(browser, live_server, title):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    browser.find_by_id('id_staff').select(1)
    browser.fill('title', title)
    browser.fill('address', 'Shillingford Road')
    browser.fill('city', 'Bolton')
    browser.fill('county', 'Greater Manchester')
    browser.fill('postcode', 'BL4')
    browser.fill('description', 'A excellent new home')
    browser.fill('price', 130000)
    browser.fill('bedrooms', 3)
    browser.fill('bathrooms', 1)
    browser.fill('livingrooms', 1)
    browser.fill('garage', 0)
    browser.attach_file('photo_main', f'{dir_path}/test_files/home6/d2f9839050024eff14e16d0429350df8e68e967b.jpg')
    browser.attach_file('photo_1', f'{dir_path}/test_files/home6/ee4822722e8088c9fe607e0225e95ec64b260846.jpg')
    browser.attach_file('photo_2', f'{dir_path}/test_files/home6/e16d3526ae1fd22eb35e9d8382761fe5f1f27789.jpg')
    browser.attach_file('photo_3', f'{dir_path}/test_files/home6/a1a6ac96797f70831e92a89ea169383ec8d911ba.jpg')
    browser.attach_file('photo_4', f'{dir_path}/test_files/home6/9368e14e8f0910c27fa39f7112d43bd6e0fafc8e.jpg')
    browser.attach_file('photo_5', f'{dir_path}/test_files/home6/6e597626f021123565dd8eb7ebad758a7ef9ed6a.jpg')
    browser.attach_file('photo_6', f'{dir_path}/test_files/home6/5d5c90ee96cfb454c097c00e241ea7e53e6988e9.jpg')


@when(parsers.parse('I update the listing title to "{title}"'))
def update_listing(browser, live_server, title):
    browser.fill('title', title)
