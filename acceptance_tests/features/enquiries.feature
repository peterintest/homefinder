@ims
Feature: Manage enquiries
  As a admin user,
  I want to login to the IMS,
  So I can manage enquiries.

  Background:
    Given a admin user is logged into the IMS

  Scenario: Read contact enquiry
    When I select contact enquiries
    And I see the "Select contact to change" page
    And I select "Jessica Smith"
    Then I see "Hello, I'm interested in arranging a viewing" message

  Scenario: Delete contact enquiry
    When I select contact enquiries
    And I see the "Select contact to change" page
    And I select "Jessica Smith"
    And I see the "Change contact" page
    And I select "Delete"
    And I see the "Are you sure?" page
    And I select the submit button
    Then I see "The contact “Jessica Smith” was deleted successfully." message

