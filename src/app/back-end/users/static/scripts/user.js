document.addEventListener("DOMContentLoaded", function() {
  var createForm = document.getElementById('createform')
  var editForm = document.getElementById('editform')
  var addAccountButton = document.querySelector('.user-name.add-account')
  var editButton = document.querySelector('.user-name')
  var saveButtons = document.querySelectorAll('form button')
  var confirmationModal = document.getElementById('confirmationModal')
  var confirmYesButton = document.getElementById('confirmYes')
  var confirmNoButton = document.getElementById('confirmNo')

  addAccountButton.addEventListener('click', function() {
    createForm.style.display = 'block'
    editForm.style.display = 'none'
  })

  editButton.addEventListener('click', function() {
    editForm.style.display = 'block'
    createForm.style.display = 'none'
  })

  saveButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
      event.preventDefault()
      confirmationModal.style.display = 'block'
    })
  })

  confirmYesButton.addEventListener('click', function() {
    confirmationModal.style.display = 'none'
  })

  confirmNoButton.addEventListener('click', function() {
    confirmationModal.style.display = 'none'
  })
})