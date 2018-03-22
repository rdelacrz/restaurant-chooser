import { Component, OnInit, ViewChild, ViewEncapsulation } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../../../core/services';
import { FileData, FullUserData } from '../../../view-models';

@Component({
  selector: 'add-user',
  templateUrl: './add-user.component.html',
  styleUrls: ['./add-user.component.scss']
})
export class AddUserComponent implements OnInit {
  @ViewChild("fileInput") fileInput;

  header = "Add User";
  model = new FullUserData(null, null, null, null, null, null);
  fileLoading = false;    // Set to true by <form-file-input> when file is in the process of loading

  constructor(private userService: UserService, private router: Router) { }

  ngOnInit() {
  }

  setFile(fileData : FileData) {
    this.model.file_data = fileData;
    this.fileLoading = false;   // Means that file has full loaded
  }

  onSubmit() {
    this.userService.createUser(this.model).subscribe(
      results => {
        
      },
      error => {

      },
      () => {
        this.goToUsersScreen();
      }
    );
  }

  onCancel() {
    this.goToUsersScreen();
  }

  onClear() {
    this.fileInput.clear();
    this.model.clear();
  }

  private goToUsersScreen() {
    this.router.navigateByUrl("users")
  }
}