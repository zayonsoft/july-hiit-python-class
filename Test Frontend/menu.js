async function menuApp() {
  const url = "http://localhost:8000/api/categories/";
  const categoryList = document.getElementById("category-list");

  try {
    const response = await fetch(url);
    const data = await response.json();
    // console.log(data);
    for (let i in data) {
      const eachItem = data[i];

      const a = document.createElement("a");
      a.classList.add("category-card");
      a.href = `./view-category-menu.html?id=${eachItem.id}`;
      a.innerHTML = `
        <div>
            <div class="name">${eachItem.name}</div>
            <div class="count">Unknown items</div>
          </div>
          <div class="arrow">&#8594;</div>
        `;
      categoryList.appendChild(a);
    }
  } catch (e) {
    // Display that something went wrong if fetch fails..
    categoryList.innerHTML = `
    <p class="category-card">Something went wrong!</p>
    `;
    console.log(e);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  menuApp();
});
