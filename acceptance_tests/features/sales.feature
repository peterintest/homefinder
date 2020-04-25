@ims
Feature: Manage sales
  As a admin user,
  I want to login to the CMS,
  So I can manage property sales.

  Background:
    Given a admin user is logged into the CMS

  Scenario: Add new sale
    When I select add sale
    And I see the "Add sale" page
    And I add a sale for the listing "Chieftain Way"
    And I select the save button
    Then I see "The sale “Chieftain Way” was added successfully." message

  Scenario: Delete sale
    When I select change sale
    And I select "Chieftain Way"
    And I see the "Change sale" page
    And I select "Delete"
    And I see the "Are you sure?" page
    And I select the submit button
    Then I see "The sale “Chieftain Way” was deleted successfully." message

  Scenario: Update sale
    When I select change sale
    And I select "Chieftain Way"
    And I see the "Change sale" page
    And I update the sale price to "550000"
    And I select the save button
    Then I see "The sale “Chieftain Way” was changed successfully." message
