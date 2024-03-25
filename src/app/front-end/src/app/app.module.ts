import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { HotelSelectorComponent } from './components/hotel-selector/hotel-selector.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatButtonModule } from '@angular/material/button';
import { AsyncPipe } from '@angular/common';
import { AppRoutingModule } from './app-routing.module';
import { MatIconModule } from '@angular/material/icon';
import { LoginComponent } from './components/login/login.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [
    AppComponent,
    HotelSelectorComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatInputModule,
    MatAutocompleteModule,
    MatFormFieldModule,
    ReactiveFormsModule,
    AsyncPipe,
    MatButtonModule,
    MatIconModule,
    NgbModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
