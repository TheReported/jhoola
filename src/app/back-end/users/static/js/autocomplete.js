function fetchHotelDetail(hotel) {
    fetch('http://localhost:8000/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',

        },
        credentials: 'include',
        body: JSON.stringify(hotel),
    })
    .then(response => {
        console.log(response)
        if (!response.ok) {
            throw new Error('Network response was not ok')
        }
        return response.json()
    })
    .then(data => {
        console.log(data)
        return data
    })
    .catch(error => {
        console.error('Error fetching hotel details:', error)
    })
}

function fetchHotels() {
    fetch('http://localhost:8000/api/hotels/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            hotels = data;
            console.log(data)
            return data
        })
        .catch(error => {
            console.error('Error fetching hotels:', error);
        });
}

function displayHotels() {
  let hotelDropdown = document.getElementById('hotel-dropdown');
  let inputValue = document.getElementById('hotel-input').value.toLowerCase();
  let filteredHotels = hotels.filter(hotel => `${hotel.name}, ${hotel.city}`.toLowerCase().includes(inputValue)).slice(0, 5);

  hotelDropdown.innerHTML = '';
  filteredHotels.forEach(hotel => {
      let listHotel = document.createElement('li');
      let displayFormat = `${hotel.name}, ${hotel.city}`;
      listHotel.textContent = displayFormat;
      listHotel.classList.add('pt-2', 'mt-1');
      listHotel.addEventListener('click', function() {
          document.getElementById('hotel-input').value = displayFormat;
          hotelDropdown.innerHTML = '';
          fetchHotelDetail(hotel)
      });
      hotelDropdown.appendChild(listHotel);
  });
  hotelDropdown.classList.add('remove-bullets');
}


document.addEventListener('DOMContentLoaded', fetchHotels);

let hotelInput = document.getElementById('hotel-input');
hotelInput.addEventListener('focus', displayHotels.bind(this));
document.getElementById('hotel-input').addEventListener('input', displayHotels);
