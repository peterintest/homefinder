from django.core.management import call_command
from selenium import webdriver
from accounts.tests.factories import UserFactory
from pytest_bdd import scenarios, given, when, then, parsers
import pytest


@pytest.fixture(scope='session')
def splinter_webdriver():
    """Override splinter webdriver name."""
    return 'chrome'


@pytest.fixture()
def django_db_setup(django_db_setup, django_db_blocker):
    """Load DB with test data"""
    with django_db_blocker.unblock():
        call_command('loaddata', 'acceptance_tests/test_data.json')


# Common BDD Steps
# Given Steps

@given('a admin user is logged into the CMS')
@given('a admin user is logged into the IMS')
def admin_home(browser, client, live_server, admin_user):
    client.login(username=admin_user.username, password='password')
    cookie = client.cookies['sessionid']
    browser.visit(live_server.url + '/admin/')
    browser.cookies.add({'sessionid': cookie.value})
    browser.reload()


# When Steps

@when(parsers.parse('I select "{text}"'))
def select_link_by_title(browser, live_server, text):
    browser.links.find_by_text(text).click()


@when(parsers.parse('I select the submit button'))
def select_submit_button(browser, live_server):
    browser.find_by_css(f"input[type=submit]").first.click()


@when(parsers.parse('I select the save button'))
def select_save_button(browser, live_server):
    browser.find_by_name('_save').first.click()


@when(parsers.parse('I see the "{heading}" page'))
def check_second_page_heading(browser, live_server, heading):
    assert browser.find_by_tag('h1')[1].value == heading


# Then Steps

@then(parsers.parse('I see "{title}" message'))
def message_is_present(browser, live_server, title):
    assert browser.is_text_present(title)

