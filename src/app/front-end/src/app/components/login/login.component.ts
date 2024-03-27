import { Component, OnInit } from '@angular/core';
import { FormControl, Validators, FormGroup } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { LoginService } from 'src/app/services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  hide = true;
  hotelSlug: string = "";
  loginForm!: FormGroup;

  constructor(private route: ActivatedRoute, private loginService: LoginService) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.hotelSlug = params['slug'];
    });

    this.loginForm = new FormGroup({
      username: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required])
    });
  }

  submitData() {
    if (this.loginForm.valid) {
      let formData = this.loginForm.value;
      this.loginService.postData(this.hotelSlug, formData).subscribe(
        (response) => {
          console.log(response);
        },
        (error) => {
          console.error('Error occurred:', error);
        }
      );
    }
  }
}
