@ims
Feature: Manage customers
  As a admin user,
  I want to login to the IMS,
  So I can manage customers.

  Background:
    Given a admin user is logged into the IMS

  Scenario: Add new customer
    When I select add customer
    And I see the "Add customer" page
    And I add a customer with the name "David Smith"
    And I select the save button
    Then I see "The customer “David Smith” was added successfully." message

  Scenario: Delete customer
    When I select change customer
    And I select "David Smith"
    And I see the "Change customer" page
    And I select "Delete"
    And I see the "Are you sure?" page
    And I select the submit button
    Then I see "The customer “David Smith” was deleted successfully." message

  Scenario: Update customer details
    When I select change customer
    And I select "David Smith"
    And I see the "Change customer" page
    And I update the customer email to "new@test.com"
    And I select the save button
    Then I see "The customer “David Smith” was changed successfully." message
