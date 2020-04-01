
let randomEmailAddress = Math.random().toString(15).substring(5) + '@gmail.com';

context('Auth User', () => {
  it('Sign Up a new user', () => {
    cy.visit('/register')
    cy.wait(1000)
    
    // Create John user
    cy.get('[data-cy=register-name]').type('John')
    
    cy.get('[data-cy=register-email]').type(randomEmailAddress)
    cy.get('[data-cy=register-password]').type('Hello World')

    cy.contains('REGISTER').click()
    
    cy.url().should('include', '/login')
  })


  it('Sign In as John, then Logout', () => {
    cy.visit('/login')
    cy.wait(1000)
    
    // Login as John user
    cy.get('[data-cy=login-email]').type(randomEmailAddress)
    cy.get('[data-cy=login-password]').type('Hello World')

    cy.contains('LOGIN').click()
    
    cy.url().should('include', '/')
    cy.wait(1000)
    
    // Logout John
    cy.contains('LOGOUT').click()
    cy.url().should('include', '/login')
  })
})