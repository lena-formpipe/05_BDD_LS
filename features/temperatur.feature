# Vi ska göra temperaturomvandling

  Feature: enkel temperaturomvandling Celsius och Fahrenheit

    Scenario: Omvandla Fahrenheit till Celsius
      Given : att jag har temperaturen 32 Fahrenheit
      When : jag omvandlar till Celsius
      Then : så ska svaret bli 0 Celsius

    Scenario: Omvandla Celsius till Fahrenheit
      Given : att jag har temperaturen 100 Celsius
      When : jag omvandlar till Fahrenheit
      Then : så ska svaret bli 212 Fahrenheit