Feature: Greeting
  Scenario: Compose the canonical salutation
    Given the recipient is "World"
    When I compose the greeting
    Then the greeting is "Hello, World!"
