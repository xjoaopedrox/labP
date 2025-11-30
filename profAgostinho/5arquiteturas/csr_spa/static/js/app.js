fetch("/posts")
  .then(res => res.json())
  .then(data => {
    const div = document.getElementById("posts");
    data.forEach(post => {
      div.innerHTML += `<h2>${post.title}</h2><p>${post.text}</p><hr>`;
    });
  });
