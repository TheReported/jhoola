setTimeout(function() {
  let messageElement = document.getElementById('message');
  if (messageElement) {
    messageElement.remove();
  }
}, 5000);