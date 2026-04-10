document.addEventListener('DOMContentLoaded', function () {
    var alerts = document.querySelectorAll('.msg[data-dismiss]');
    alerts.forEach(function (el) {
        setTimeout(function () {
            el.style.transition = 'opacity 0.4s';
            el.style.opacity = '0';
            setTimeout(function () { if (el.parentNode) el.remove(); }, 400);
        }, 4000);
    });

    var readBar = document.querySelector('.mobile-price-bar');
    if (readBar) {
        document.body.classList.add('has-read-bar');
    }
});
