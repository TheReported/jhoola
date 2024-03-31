import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HotelSelectorComponent } from './components/hotel-selector/hotel-selector.component';
import { LoginComponent } from './components/login/login.component';
import { AdminDashboardComponent } from './components/admin-dashboard/admin-dashboard.component';

const routes: Routes = [
  { path: "", component: HotelSelectorComponent},
  { path: "login/:slug", component: LoginComponent},
  { path: "dashboard", component: AdminDashboardComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
