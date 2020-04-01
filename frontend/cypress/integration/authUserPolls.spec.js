context('Auth User Polls', () => {
  it('Create poll as logged user', () => {
    cy.login()
    
    // Check if user doesnt' has any polls
    cy.visit('/polls')
    cy.wait(1000)
    
    cy.contains('Nothing here...')
    cy.contains('CREATE POLL').click()
    
    cy.url().should('include', '/create')
    cy.wait(1000)
    
    // Create a new poll
    cy.get('[data-cy=question-input]').type('What do you want to eat?')
    
    cy.get('[data-cy=option-input]').type('Sandwich with ham!')
    cy.contains('ADD OPTION').click()
    
    cy.get('[data-cy=option-input]').type('Chicken!')
    cy.contains('ADD OPTION').click()
    
    cy.contains('CREATE').click()
    
    // Check if user has polls
    cy.visit('/polls')
    cy.wait(1000)
    
    cy.contains('What do you want to eat?')
    cy.contains('CREATE POLL')
  })
})