// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms'; // Importa FormsModule
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { HotelSelectorComponent } from './components/hotel-selector/hotel-selector.component';

@NgModule({
  declarations: [
    AppComponent,
    HotelSelectorComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
