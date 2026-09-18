# Vi ska göra temperaturomvandling

  Feature: enkel temperaturomvandling Celsius och Fahrenheit

    Scenario Outline: Omvandla Fahrenheit till Celsius
      Given att jag har temperaturen <fahrenheit> Fahrenheit
      When jag omvandlar till Celsius
      Then ska svaret bli <celsius> Celsius
      Examples:
        |fahrenheit|celsius|
        | 32       |0     |
        | 212      |100   |
        | -40      |-40   |
        | 68       |20    |

    Scenario Outline: Omvandla Celsius till Fahrenheit
      Given att jag har temperaturen <celsius> Celsius
      When jag omvandlar till Fahrenheit
      Then ska svaret bli <fahrenheit> Fahrenheit
      Examples:
        | celsius | fahrenheit |
        | 0       | 32         |
        | 100     | 212        |
        | -40     | -40        |
