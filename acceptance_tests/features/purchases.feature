@ims
Feature: Manage purchases
  As a admin user,
  I want to login to the CMS,
  So I can manage property purchases.

  Background:
    Given a admin user is logged into the CMS

  Scenario: Add new purchase
    When I select add purchase
    And I see the "Add purchase" page
    And I add a purchase for the listing "Chieftain Way"
    And I select the save button
    Then I see "The purchase “Chieftain Way” was added successfully." message

  Scenario: Delete purchase
    When I select change purchase
    And I select "Chieftain Way"
    And I see the "Change purchase" page
    And I select "Delete"
    And I see the "Are you sure?" page
    And I select the submit button
    Then I see "The purchase “Chieftain Way” was deleted successfully." message

  Scenario: Update purchase
    When I select change purchase
    And I select "Chieftain Way"
    And I see the "Change purchase" page
    And I update the purchase price to "550000"
    And I select the save button
    Then I see "The purchase “Chieftain Way” was changed successfully." message

