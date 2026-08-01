const main = document.querySelector('main');

console.log('Hello World!');

main.addEventListener('click', e =>{

    console.log(e.target);

    if (e.target.classList.contains('left-arrow')){

        const container = e.target.nextElementSibling;
        console.log(container.childern);
        console.log(container);
        container.scrollLeft -= 500;

    }

    if (e.target.classList.contains('right-arrow')){

        const container = e.target.previousElementSibling;
        console.log(container.childern);
        console.log(container);
        container.scrollLeft += 500;

    }

});