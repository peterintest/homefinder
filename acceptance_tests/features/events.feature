@ims
Feature: Manage events
  As a admin user,
  I want to login to the IMS,
  So I can manage events.

  Background:
    Given a admin user is logged into the IMS

  Scenario: Add new event
    When I select add event
    And I see the "Add event" page
    And I add an event with the title "Estate Agent Training"
    And I select the save button
    Then I see "The event “Estate Agent Training” was added successfully." message

  Scenario: Delete event
    When I select change event
    And I select "Property & Development Conference"
    And I see the "Change event" page
    And I select "Delete"
    And I see the "Are you sure?" page
    And I select the submit button
    Then I see "The event “Property & Development Conference” was deleted successfully." message

  Scenario: Update event details
    When I select change event
    And I select "Property & Development Conference"
    And I see the "Change event" page
    And I update the event title to "Property Conference"
    And I select the save button
    Then I see "The event “Property Conference” was changed successfully." message
