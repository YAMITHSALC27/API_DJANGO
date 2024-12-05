const productContainers = document.querySelectorAll('.product');

// Get the navigation buttons
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

// Keep track of the current index
let currentIndex = 0;

// Function to display the current products
function displayProducts() {
    productContainers.forEach((container, index) => {
    if (index >= currentIndex && index < currentIndex + 4) {
        container.style.display = 'block';
    } else {
        container.style.display = 'none';
    }
    });
}

// Event listener for the previous button
prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 4 + productContainers.length) % productContainers.length;
    displayProducts();
});

// Event listener for the next button
nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 4) % productContainers.length;
    displayProducts();
});

// Initial display of the products
displayProducts();
