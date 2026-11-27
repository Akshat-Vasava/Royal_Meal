let searchForm = document.querySelector('.search-form');
let loginForm = document.querySelector('.login-form');

document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
};

document.querySelector('#user-btn').onclick = () => {
    loginForm.classList.toggle('active');
};