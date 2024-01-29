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
    likeCountElement.innerHTML = `Likes: ${likeCount}`;
    console.log(likeCount);
  }
}

// function followUnfollow(id) {
//   console.log(id);
//   fetch(`/follow_unfollow/${id}`)
//     .then((response) => {
//       // console.log(response);
//       // if (!response.ok) {
//       //   throw new Error('Network response was not ok');
//       // }
//       return response.json();
//     })
//     .then((result) => {
//       console.log(result.message);
//       console.log(result);
//       console.log(user.is_following);

//       const followBtn = document.getElementById('followBtn');
//       const userId = result.user_info.id;
//       const username = result.user_info.username;
//       const followersCount = result.user_info.followers_count;
//       const followingCount = result.user_info.following_count;

//       const isOwnProfile = user === result.user_id;

//       if (isOwnProfile) {
//         console.log(
//           "This is the user's own profile. Do not perform follow/unfollow actions."
//         );
//         return;
//       }
//       if (followBtn) {
//         followBtn.innerText = result.is_following ? 'Unfollow' : 'Follow';
//       }

//       if (followersCount) {
//         followersCount.innerText = `Followers: ${followersCount}`;
//       }

//       if (followingCount) {
//         followingCount.innerText = `Followers: ${followingCount}`;
//       }
//     })
//     .catch((err) => console.error('Error:', err));
// }

async function followUnfollow(user_id) {
  fetch(`/follow_unfollow/${user_id}`, {
    method: 'POST',
  })
    .then((response) => response.json())
    .then((result) => {
      document.getElementById('follow-btn').innerHTML = `${result.stat}`;
      document.getElementById(
        'follow-data'
      ).innerHTML = `Followers: ${result.followers} | Following: ${result.following}`;
    });

  false;
}

function redirectToFollowingPage() {
  window.location.href = '/following/';
}
