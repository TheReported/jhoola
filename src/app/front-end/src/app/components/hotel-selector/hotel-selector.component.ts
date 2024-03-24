import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { HotelService } from 'src/app/services/hotel.service';

@Component({
  selector: 'app-hotel-selector',
  templateUrl: './hotel-selector.component.html',
  styleUrls: ['./hotel-selector.component.scss']
})
export class HotelSelectorComponent implements OnInit {
  hotelsControl = new FormControl();
  filteredHotels!: Observable<any[]>;
  hotels!: any[];
  maxResults = 5;

  constructor(private hotelService: HotelService) { }

  ngOnInit(): void {
    this.hotelService.getHotels().subscribe(hotels => {
      this.hotels = hotels;
      this.filteredHotels = this.hotelsControl.valueChanges.pipe(
        startWith(''),
        map(value => this._filterHotels(value))
      );
    });
  }

  private _filterHotels(value: string): any[] {
    let filteredHotels = this.hotels.filter(hotel => {
      let name = hotel.name.includes(value);
      let city = hotel.city.includes(value);
      return name || city;
    });

    return filteredHotels.slice(0, this.maxResults);
  }
  
}
