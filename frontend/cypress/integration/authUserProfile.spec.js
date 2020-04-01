context('Auth User Profile', () => {
  it('Change user account information', () => {
    cy.login()
    
    // Update user name
    cy.visit('/profile')
    cy.wait(1000)
    
    cy.get('[data-cy=profile-name]').should('have.value', 'Adam')
    
    cy.get('[data-cy=profile-name]').clear().type('Bob')
    cy.contains('UPDATE').click()
    
    cy.reload()
    cy.get('[data-cy=profile-name]').should('have.value', 'Bob')
  })
})