document.addEventListener('DOMContentLoaded', function () {
  console.log('helllooooo');
  // By default, load all posts
  load_posts();
});

function load_posts(id) {
  console.log(id);
  const postsView = document.querySelector('#posts-view');

  console.log(title);

  // Show all posts
  fetch(`profile/${user_id}`)
    .then((response) => response.json())
    .then((item) => {
      console.log(item);
    });
}
