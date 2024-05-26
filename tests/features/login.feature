Feature: Login and log out

    Scenario Outline: As a User I want to log in
        Given I am logged in as <userType> user
        Examples:
            | userType                |
            | standard_user           |
            | problem_user            | 
            | performance_glitch_user |

