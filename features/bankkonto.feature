# Vi ska göra ett bankkonto för insättning och uttag

  Feature: Skapa bankkonto som kan hantera insättning, uttag och ränta

    @smoke
    Scenario: Skapa nytt konto för en kund
      When jag skapar ett nytt konto för kunden Kalle
      Then ska startsaldot vara 0 kr


    Scenario: Sätta in pengar på kontot
     Given att Kalle har ett konto med saldo 0 kr
     When han sätter in 100 kr
     Then ska saldot vara 100 kr


    Scenario: Ta ut pengar från kontot
      Given att Kalle har ett konto med saldo 100 kr
      When han gör ett uttag på 70 kr
      Then ska saldot vara 30 kr


    Scenario: Ränta på kontot
      Given att Kalle har ett konto med saldo 100 kr
      When räntan 5% appliceras på kontot
      Then ska saldot vara 105 kr