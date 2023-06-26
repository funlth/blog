/* add_video.js */
var form = document.querySelector('form');
var titleInput = form.querySelector('#id_title');
var descriptionTextarea = form.querySelector('#id_description');
var urlInput = form.querySelector('#id_url');

form.addEventListener('submit', function(event) {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Create a new video object with the form data
  var newVideo = {
    title: titleInput.value.trim(),
    description: descriptionTextarea.value.trim(),
    url: urlInput.value.trim()
  };

  // Send a POST request to the server to add the new video
  fetch('/add_video/', {
    method: 'POST',
    body: JSON.stringify(newVideo),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(function(response) {
    if (response.ok) {
      // If the response is successful, redirect to the new video's detail page
      return response.json();
    } else {
      // If the response is not successful, throw an error
      throw new Error('Failed to add video.');
    }
  })
  .then(function(data) {
    window.location.href = `/video/${data.id}/`;
  })
  .catch(function(error) {
    // Handle errors
    alert(error.message);
  });
});