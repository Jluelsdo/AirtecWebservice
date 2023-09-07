const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    if (link.href === window.location.href && link.getAttribute('href') !== '') {
        link.classList.add('active');
    }
    link.addEventListener('click', function(event) {
        if (link.getAttribute('href') === '') {
            return;
        }
        event.preventDefault();
        navLinks.forEach(link => link.classList.remove('active'));
        this.classList.add('active');
        window.location.href = this.href;
    });
});