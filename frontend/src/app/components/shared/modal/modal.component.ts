import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { ModalService } from '../../../core/services';

@Component({
  selector: 'modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.scss']
})
export class ModalComponent implements OnInit {
  @ViewChild('modalContent') modalTrigger : ElementRef;

  constructor(public modalService: ModalService) {}

  ngOnInit() {
    this.modalService.setModalTemplate(this.modalTrigger);
  }
}
