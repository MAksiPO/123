var slideIndex = 1;
        var timer = null;
        showSlides(slideIndex)
        afterTime(2000); // Устанавливаем считчик...
        /* Функция увеличивает индекс на 1, показывает следующй слайд*/
        function plusSlide() {
            showSlides(slideIndex += 1);
        }
 
        /* Функция уменьшяет индекс на 1, показывает предыдущий слайд*/
        function minusSlide() {
            showSlides(slideIndex -= 1);
        }
 
        /* Устанавливает текущий слайд */
        function currentSlide(n) {
            console.log(n);
            showSlides(slideIndex = n);
        }
 