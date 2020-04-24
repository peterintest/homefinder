import pytest
from pytest_bdd import scenarios, given, when, parsers

pytestmark = pytest.mark.webtest

# Scenarios

scenarios('../features/events.feature')


# When Steps

@when('I select add event')
def select_add_event(browser, live_server):
    browser.links.find_by_partial_href(f'/event/add/').click()


@when('I select change event')
def select_change_event(browser, live_server):
   browser.links.find_by_href('/admin/events/event/').click()


@when(parsers.parse('I add an event with the title "{title}"'))
def add_event(browser, live_server, title):
    browser.fill('title', title)
    browser.fill('description', 'Popular property conference')
    browser.fill('location', 'London')
    browser.find_by_id('id_organiser').select(1)


@when(parsers.parse('I update the event title to "{title}"'))
def update_event(browser, live_server, title):
    browser.fill('title', title)
