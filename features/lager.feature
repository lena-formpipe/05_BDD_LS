# Lagerhållning

Feature: Lagersaldo ska blir rätt efter ändringar i varor.

  Scenario: Öka varor i lagret
    Given att jag har ett lager
    Given att lagersaldo för bananer = 0
    When jag lägger till 5 bananer
    Then så ska lagersaldot vara 5 bananer

  Scenario: Minska varor i lagret
    Given att jag har ett lager
    Given att lagersaldo för bananer = 10
    When jag tar bort 3 bananer
    Then så ska lagersaldot vara 7 bananer

