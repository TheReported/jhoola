document.addEventListener("DOMContentLoaded", function() {
  var createForm = document.getElementById('createform')
  var editForm = document.getElementById('editform')
  var addAccountButton = document.querySelector('.add-account')
  var editButtons = document.querySelectorAll('.user-name')
  var saveButtons = document.querySelectorAll('form button')

  addAccountButton.addEventListener('click', function() {
    createForm.style.display = 'block'
    editForm.style.display = 'none'
  })

  editButtons.forEach((button) => {
    button.addEventListener('click', function() {
      editForm.style.display = 'block'
      createForm.style.display = 'none'
    })
  })
  
})