import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FileData, FullUserData } from '../../view-models';
import { ModalService, UserService } from '../../core/services';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent implements OnInit {
  header = "Users";
  users : any;

  constructor(private domSanitizer: DomSanitizer, private modalService: ModalService, private router: Router, 
    private userService: UserService) { }

  ngOnInit() {
    this.users = this.userService.getUsers();
  }

  buildImgSrc(fileData: FileData) {
    let base64Image = "data:" + fileData.file_type + ";base64, " + fileData.base_64_data;
    return this.domSanitizer.bypassSecurityTrustUrl(base64Image);
  }

  onAddUser() {
    this.router.navigateByUrl("/add-user");
  }

  promptUserDetails(user: FullUserData) {
    this.modalService.activateModal("User Info", user.first_name + " " + user.last_name);
  }
}