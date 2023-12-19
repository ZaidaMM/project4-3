function getCookie(cname) {
  const name = `; ${document.cookie}`;
  const csplit = name.split(`; ${cname}=`);
  if (csplit.length == 2) return csplit.pop().split(';').shift();
}

function submitHandler(id) {
  const textareaContent = document.querySelector(`#textarea_${id}`).value;
  const content = document.querySelector(`#content_${id}`);
  const modal = document.querySelector(`#modal_edit_${id}`);

  fetch(`/edit/${id}`, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({ content: textareaContent }),
  })
    .then((response) => response.json())
    .then((result) => {
      content.innerHTML = result.data;

      // Change state like in hidden modal
      modal.classList.remove('show');
      modal.setAttribute('aria-hidden', 'true');
      modal.setAttribute('style', 'display: none');

      // Get modal backdrops
      const modalsBackdrops = document.getElementsByClassName('modal-backdrop');

      // Remove every modal backdrop
      for (let i = 0; i < modalsBackdrops.length; i++) {
        document.body.removeChild(modalsBackdrops[i]);
      }
    });
}
