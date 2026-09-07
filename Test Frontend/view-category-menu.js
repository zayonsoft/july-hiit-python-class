async function viewCategoryMenuApp() {
  const params = new URLSearchParams(window.location.search);
  const categoryId = params.get("id");
  const menuUrl = `http://localhost:8000/api/menu/?category_id=${categoryId}`;
  const menuCategoryUrl = `http://localhost:8000/api/categories/${categoryId}/`;
  const contentDiv = document.getElementById("category-list");
  //   fetch the specific ID
  try {
    // Fetch menu based on the category ID
    const title = document.querySelector("title");
    const pageTitle = document.getElementById("top");
    const menuCategoryResponse = await fetch(menuCategoryUrl);
    const menuCategoryData = await menuCategoryResponse.json();
    if (menuCategoryResponse.ok) {
      pageTitle.innerHTML = `Category - ${menuCategoryData.name}`;
      title.innerHTML = `Menu Category - ${menuCategoryData.name}`;
    } else {
      title.innerHTML = `Menu Category - Not Found`;
      contentDiv.innerHTML = "Category Not Found";
      return;
    }
  } catch (e) {
    title.innerHTML = `Menu Category - Error occured`;
    contentDiv.innerHTML = "An error occured";
    return;
  }

  try {
    // Fetch menu based on the category ID
    const menuResponse = await fetch(menuUrl);
    const menuData = await menuResponse.json();
    if (menuData.length == 0) {
      contentDiv.innerHTML = `
        <div class="content-div">
        <p>No item found!</p>
        </div>
        `;
      return;
    }

    menuData.forEach((menu) => {
      const eachContentDiv = document.createElement("div");
      eachContentDiv.classList.add("category-card");
      eachContentDiv.innerHTML = `
        <div class="content-div">
            <div class="name">Name: ${menu.name}</div>
            <div class="count">Desc: ${menu.description}</div>
            <div class="count">Price: ${menu.price}</div>
          </div>
        `;
      contentDiv.appendChild(eachContentDiv);
    });
  } catch (e) {}
}

document.addEventListener("DOMContentLoaded", viewCategoryMenuApp);
