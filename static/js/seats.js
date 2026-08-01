const seatsContainer    = document.querySelector('.seats');
const seats             = document.querySelectorAll('.row .seat:not(.occupied):not(.empty)');

console.log(seatsContainer);
console.log(seats);

seatsContainer.addEventListener('click', e =>{

    console.log(e.target);
    if(e.target.classList.contains('seat') &&
        !e.target.classList.contains('occupied') &&
        !e.target.classList.contains('empty')){

        const seat = e.target;
        const row = seat.closest('.row');
        
        const rowIndex = [...document.querySelectorAll('.row')].indexOf(row);
        const seatIndex = [...row.children].indexOf(seat);

        console.log(`Row: ${rowIndex}, Seat: ${seatIndex}`);

        e.target.classList.toggle('selected');

    }

});