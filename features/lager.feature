# Lagerhållning
Feature: Lagersaldo ska blir rätt efter ändringar i varor.

  Scenario Outline: Öka varor i lagret
    Given att jag har ett lager
    Given att lagersaldo för <item> är <saldo_before> st
    When jag lägger till <amount_added> st <item>
    Then ska lagersaldot vara <saldo_after> st <item>
    Examples:
     |item  |saldo_before|amount_added|saldo_after|
     |äpplen | 0           |5          | 5         |
     |bananer | 10          |15         | 25        |


  Scenario Outline: Minska varor i lagret
    Given att jag har ett lager
    Given att lagersaldo för <item> är <saldo_before> st
    When jag tar bort <amount_removed> st <item>
    Then ska lagersaldot vara <saldo_after> st <item>
    Examples:
      |item|saldo_before|amount_removed|saldo_after|
      |äpplen | 10         |5             | 5         |
      |bananer| 100        |15            | 85        |

