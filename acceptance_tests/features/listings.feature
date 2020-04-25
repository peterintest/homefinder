@cms
Feature: Manage property listings
  As a admin user,
  I want to login to the CMS,
  So I can manage property listings.

  Background:
    Given a admin user is logged into the CMS

  Scenario: Add new property listing
    When I select add listing
    And I see the "Add listing" page
    And I add a listing with the title "Shillingford Road"
    And I select the save button
    Then I see "The listing “Shillingford Road” was added successfully." message

  Scenario: Delete property listing
    When I select change listing
    And I select "Chieftain Way"
    And I see the "Change listing" page
    And I select "Delete"
    And I see the "Are you sure?" page
    And I select the submit button
    Then I see "The listing “Chieftain Way” was deleted successfully." message

  Scenario: Update property listing
    When I select change listing
    And I select "Motcomb Street"
    And I see the "Change listing" page
    And I update the listing title to "Motcomb Road"
    And I select the save button
    Then I see "The listing “Motcomb Road” was changed successfully." message

  Scenario: Make property listing private
    When I select change listing
    And I select "Motcomb Street"
    And I see the "Change listing" page
    And I uncheck is published
    And I select the save button
    Then I see "The listing “Motcomb Street” was changed successfully." message
