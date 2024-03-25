import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { HotelService } from 'src/app/services/hotel.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-hotel-selector',
  templateUrl: './hotel-selector.component.html',
  styleUrls: ['./hotel-selector.component.scss']
})
export class HotelSelectorComponent implements OnInit {
  hotelInput = new FormControl();
  filteredHotels!: Observable<any[]>;
  hotels!: any[];
  maxResults = 5;

  constructor(private hotelService: HotelService, private router: Router) { }

  ngOnInit(): void {
    this.hotelService.getHotels().subscribe(hotels => {
      this.hotels = hotels;
      this.filteredHotels = this.hotelInput.valueChanges.pipe(
        startWith(''),
        map(value => this._filterHotels(value))
      );
    });
  }

  private _filterHotels(value: string): any[] {
    let formattedValue = value.toLowerCase();

    let filteredHotels = this.hotels.filter(hotel => {
      let name = hotel.name.toLowerCase().includes(formattedValue);
      let city = hotel.city.toLowerCase().includes(formattedValue);
      return name || city;
    });

    return filteredHotels.slice(0, this.maxResults);
  }

  formatSlug(hotelName: string): string{
    const nonAcceptedValues = /[&\s]+/g
    const normalizedAccents = hotelName.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    let slug = normalizedAccents.toLowerCase().replace(nonAcceptedValues, '-');
    return slug;
  }

  redirectToLogin(): void {
    let hotelName = this.hotelInput.value.split(',')[0].trim();
    let slug = this.formatSlug(hotelName);
    this.router.navigate(['/login', slug]);
  }

}
