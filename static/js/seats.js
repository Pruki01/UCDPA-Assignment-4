const seatsContainer    = document.querySelector('.seats');
const seats             = document.querySelectorAll('.row .seat:not(.occupied):not(.empty)');
const btn               = document.querySelector('.tickets-btn');

console.log(seatsContainer);
console.log(seats);

const rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];

function getSelectedSeats(){
    
    return [...document.querySelectorAll('.seat.selected')].map(seat => {
        const row = seat.closest('.row');

        const rowIndex = [...document.querySelectorAll('.row')].indexOf(row);
        const seatIndex = [...row.children].indexOf(seat);

        return {
            row: rows[rowIndex],
            seat: seatIndex
        }
    }
    )
}

seatsContainer.addEventListener('click', e =>{

    console.log(e.target);
    if(e.target.classList.contains('seat') &&
        !e.target.classList.contains('occupied') &&
        !e.target.classList.contains('empty')){

        e.target.classList.toggle('selected');

    }

});

btn.addEventListener('click', () => {
    console.log(getSelectedSeats());

    fetch('/api/selected-seats', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(getSelectedSeats())
    })
});