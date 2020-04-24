import os
import pytest
from pytest_bdd import scenarios, given, when, parsers

pytestmark = pytest.mark.webtest

# Scenarios

scenarios('../features/staff.feature')


# When Steps

@when('I select add staff')
def select_add_staff(browser, live_server):
    browser.links.find_by_partial_href(f'/staff/add/').click()


@when('I select change staff')
def select_change_staff(browser, live_server):
   browser.links.find_by_href('/admin/staff/staff/').click()


@when(parsers.parse('I add a staff member with the name "{name}"'))
def add_staff(browser, live_server, name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    browser.fill('name', name)
    browser.fill('job_title', 'Estate Agent')
    browser.fill('phone', '012345678912')
    browser.fill('email', 'test@test.com')
    browser.fill('photo', f'{dir_path}/test_files/staff/person.png')
    browser.fill('start_date_0', '2020-04-01')
    browser.fill('start_date_1', '10:00:00')


@when(parsers.parse('I update the staff job title to "{job_title}"'))
def update_staff(browser, live_server, job_title):
    browser.fill('job_title', job_title)
