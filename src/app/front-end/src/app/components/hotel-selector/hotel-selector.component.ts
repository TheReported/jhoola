// hotel-selector.component.ts
import { Component, OnInit } from '@angular/core';
import { HotelService } from 'src/app/services/hotel.service';

@Component({
  selector: 'app-hotel-selector',
  templateUrl: './hotel-selector.component.html',
  styleUrls: ['./hotel-selector.component.scss']
})
export class HotelSelectorComponent implements OnInit {
  hotels: any[] = [];
  selectedHotel: any;

  constructor(private hotelService: HotelService) { }

  ngOnInit(): void {
    this.getHotels();
  }

  getHotels(): void {
    this.hotelService.getHoteles()
      .subscribe(hotels => this.hotels = hotels);
  }
}
