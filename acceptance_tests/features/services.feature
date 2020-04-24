@ims
Feature: Manage services
  As a admin user,
  I want to login to the IMS,
  So I can manage services.

  Background:
    Given a admin user is logged into the IMS

  Scenario: Add new service
    When I select add service
    And I see the "Add service" page
    And I add a service with the name "Removals"
    And I select the save button
    Then I see "The service “Removals” was added successfully." message

  Scenario: Delete service
    When I select change service
    And I select "Independent mortgage brokerage"
    And I see the "Change service" page
    And I select "Delete"
    And I see the "Are you sure?" page
    And I select the submit button
    Then I see "The service “Independent mortgage brokerage” was deleted successfully." message

  Scenario: Update service name
    When I select change service
    And I select "Independent mortgage brokerage"
    And I see the "Change service" page
    And I update the service name to "Property Evaluation"
    And I select the save button
    Then I see "The service “Property Evaluation” was changed successfully." message
