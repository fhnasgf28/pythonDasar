const form = document.getElementById('rentalForm');
const nameInput = document.getElementById('name');
const durationInput = document.getElementById('duration');
const totalPriceDiv = document.getElementById('totalPrice');
const renterList = document.getElementById('renterList');

const pricePerHour = 5000;

form.addEventListener('submit', function(e) {
    e.preventDefault();

    const name = nameInput.value.trim();
    const duration = parseInt(durationInput.value);

    if (name === '' || isNaN(duration) || duration <= 0) {
        alert('Please enter a valid name and duration.');
        return;
    }

    const total = duration * pricePerHour;
    totalPriceDiv.textContent = `${name} harus membayar Rp ${total.toLocaleString()}`;
    const li = document.createElement('li');
    li.textContent = `${name} menyewa selama ${duration} jam, total Rp ${total.toLocaleString()}`;
    renterList.appendChild(li);

    // reset the form
    form.reset();
})