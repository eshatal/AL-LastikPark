<script>
        const slider = document.querySelector('.slider');
        const prevButton = document.querySelector('.prev');
        const nextButton = document.querySelector('.next');

        prevButton.addEventListener('click', () => {
            slider.scrollBy({
                left: -220,
                behavior: 'smooth'
            });
        });

        nextButton.addEventListener('click', () => {
            slider.scrollBy({
                left: 220,
                behavior: 'smooth'
            });
        });
    </script>