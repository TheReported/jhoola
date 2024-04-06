filterHotels(value); {
  let formattedValue = value.toLowerCase();

  let filteredHotels = this.hotels.filter(hotel => {
      let name = hotel.name.toLowerCase().includes(formattedValue);
      return name
  });

  return filteredHotels;
}
