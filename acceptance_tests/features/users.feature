@ims
Feature: Manage users
  As a admin user,
  I want to login to the IMS,
  So I can manage users.

  Background:
    Given a admin user is logged into the IMS

  Scenario: Add new user
    When I select add user
    And I see the "Add user" page
    And I add a user with the username "david"
    And I select the save button
    Then I see "The user “david” was added successfully." message

  Scenario: Delete user
    When I select change user
    And I select "oliver"
    And I see the "Change user" page
    And I select "Delete"
    And I see the "Are you sure?" page
    And I select the submit button
    Then I see "The user “oliver” was deleted successfully." message

  Scenario: Update user details
    When I select change user
    And I select "oliver"
    And I see the "Change user" page
    And I select change password
    And I see the "Change password: oliver" page
    And I update the user password to "another_secure_password"
    And I select the submit button
    Then I see "Password changed successfully." message
