import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HotelSelectorComponent } from './components/hotel-selector/hotel-selector.component';
import { LoginComponent } from './components/login/login.component';

const routes: Routes = [
  { path: "", component: HotelSelectorComponent},
  { path: "login/:slug", component: LoginComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
