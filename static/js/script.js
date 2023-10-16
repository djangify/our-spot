const btn = document.querySelector(".like-btn");

btn.addEventListener("click", () => {
  const slug = btn.dataset.slug;
  const url = `/locations/${slug}/like/`;

  fetch(url, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      btn.dataset.likes = data.likes_count;
      btn.querySelector(".likes-count").textContent = data.likes_count;
    });
});
