var checkbox = document.getElementById('checkbox');
var profile = document.querySelector('.profile');
var footer = document.querySelector('.footer-mini');
var mailto = document.querySelector('.footer-mail');


function toggleClick() {
    document.body.classList.toggle('dark');
    mailto.classList.toggle('footer-mail-dark');
    profile.classList.toggle('profile-dark');
    footer.classList.toggle('footer-mini-dark');
}
checkbox.addEventListener('click',toggleClick);

