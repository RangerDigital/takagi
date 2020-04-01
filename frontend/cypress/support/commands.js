// Create a new user, and log in.
Cypress.Commands.add("login", () => {
  let randomEmailAddress = Math.random().toString(15).substring(5) + '@gmail.com';
  
  cy.request({
    method: 'POST',
    url: 'http://127.0.0.1:5000/users/register',
    body: {
      name: 'Adam',
      email: randomEmailAddress,
      password: 'Hello World'
    }
  })
  
  cy.request({
    method: 'POST',
    url: 'http://127.0.0.1:5000/users/login',
    body: {
      email: randomEmailAddress,
      password: 'Hello World'
    }
  }).then((response) => {
    localStorage.setItem('jwt_token', response.body.jwt_token)
  })
});