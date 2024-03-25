import { Component, OnInit } from '@angular/core';
import { FormControl,Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  hide = true;
  hotelSlug: string = '';
  username = new FormControl('', [Validators.required])
  password = new FormControl('', [Validators.required])

  constructor(private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.hotelSlug = params['hotelSlug'];
      // Ahora puedes utilizar this.hotelSlug en tu lógica de autenticación
    });
  }
}
