import pytest
from pytest_bdd import scenarios, given, when, parsers

pytestmark = pytest.mark.webtest

# Scenarios

scenarios('../features/enquiries.feature')


# When Steps

@when('I select contact enquiries')
def select_contact_enquiries(browser, live_server):
   browser.links.find_by_href('/admin/contacts/contact/').click()
