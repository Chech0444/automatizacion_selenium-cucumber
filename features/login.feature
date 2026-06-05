Feature: Login
  Como usuario quiero iniciar sesion para acceder al dashboard

  Background:
    Given la app esta corriendo

  Scenario: Login exitoso con credenciales validas
    When voy a la pagina de login
    And ingreso "admin" en el campo "username"
    And ingreso "1234" en el campo "password"
    And hago click en "Ingresar"
    Then veo el texto "Bienvenido admin!"

  Scenario: Login fallido con credenciales invalidas
    When voy a la pagina de login
    And ingreso "admin" en el campo "username"
    And ingreso "wrong" en el campo "password"
    And hago click en "Ingresar"
    Then veo el texto "Credenciales invalidas"
