@ims
Feature: Manage staff
  As a admin user,
  I want to login to the IMS,
  So I can manage staff.

  Background:
    Given a admin user is logged into the IMS

  Scenario: Add new staff
    When I select add staff
    And I see the "Add staff" page
    And I add a staff member with the name "David Jones"
    And I select the save button
    Then I see "The staff “David Jones” was added successfully." message

  Scenario: Delete staff
    When I select change staff
    And I select "James Smith"
    And I see the "Change staff" page
    And I select "Delete"
    And I see the "Are you sure?" page
    And I select the submit button
    Then I see "The staff “James Smith” was deleted successfully." message

  Scenario: Update staff details
    When I select change staff
    And I select "James Smith"
    And I see the "Change staff" page
    And I update the staff job title to "Property Sales Manager"
    And I select the save button
    Then I see "The staff “James Smith” was changed successfully." message
