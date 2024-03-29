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

      content.innerHTML = result.data;

      // Close the modal
      $(modal).modal('hide');
    })
    .catch((error) => {
      console.error('Error:', error.message);
    });
}

function likeHandler(id, postsLiked) {
  console.log(id);
  const btn = document.getElementById(`${id}`);

  // Toggle between 'fa-heart' and 'fa-heart-o' classes
  btn.classList.toggle('fa-heart');
  btn.classList.toggle('fa-heart-o');

  const liked = postsLiked.includes(id);

  if (liked) {
    fetch(`/add_unlike/${id}`)
      .then((response) => response.json())
      .then((result) => {
        console.log(result);
        updateLikeCount(id, result.like);
        console.log(result.like);
      })
      .catch((err) => console.error('Error:', err))
      .finally(() => {
        console.log('Fetched, unliked');
      });
  } else {
    fetch(`/add_like/${id}`)
      .then((response) => response.json())
      .then((result) => {
        console.log(result);
        updateLikeCount(id, result.like);
        console.log(result.like);
      })
      .catch((err) => console.error('Error:', err))
      .finally(() => {
        console.log('Fetched, liked');
      });
  }
}

function updateLikeCount(postId, likeCount) {
  const likeCountElement = document.getElementById(`like_count_${postId}`);
  if (likeCountElement) {
    const likePlural = likeCount === 1 ? 'like' : 'likes';
    likeCountElement.innerHTML = `Likes: ${likeCount} ${likePlural}`;
  }
  console.log(likeCount);
}
