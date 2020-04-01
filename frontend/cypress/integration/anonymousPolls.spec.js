context('Anonymous Polls', () => {
  it('Create a new poll', () => {
    cy.visit('/')
    
    // Get to Create view
    cy.contains('CREATE POLL').click()
    cy.url().should('include', '/create')
    
    cy.get('[data-cy=question-input]').type('What do you want to eat?')
    
    cy.get('[data-cy=option-input]').type('Sandwich with ham!')
    cy.contains('ADD OPTION').click()
    
    // Delete first option
    cy.contains('Sandwich with ham!').click()
    
    cy.get('[data-cy=option-input]').type('Sandwich with ham!')
    cy.contains('ADD OPTION').click()
    
    cy.get('[data-cy=option-input]').type('Chicken!')
    cy.contains('ADD OPTION').click()
    
    cy.contains('CREATE').click()
  })
  
  it('Vote in poll', () => {
    cy.url().should('include', '/polls/')
    cy.wait(1000)
    
    // Vote for Chicken option
    cy.contains('Chicken!').click()
    cy.contains('VOTE').click()
  })
  
  it('Check poll results', () => {
    cy.url().should('include', '/results')
    cy.wait(1000)
    
    // Check if option was checked
    cy.contains('What do you want to eat?')
    cy.contains('1 Votes')
    
    cy.contains('100 %')
    cy.contains('0 %')
  })
})