import { ElementRef, Injectable } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';

@Injectable()
export class ModalService {
  private modalTemplate : ElementRef;
  public modalTitle : string;
  public modalMessage : string;
  public active : boolean = false;

  constructor(private ngbModal: NgbModal) {}

  // Should be called by modal component on startup
  setModalTemplate(modalTemplate: ElementRef) {
    this.modalTemplate = modalTemplate;
  }

  activateModal(modalTitle: string, modalMessage: string) {
    this.modalTitle = modalTitle;
    this.modalMessage = modalMessage;
    if (this.modalTemplate) {
      this.active = true;
      this.open();
    }
  }

  open() {
    this.ngbModal.open(this.modalTemplate).result.then((result) => {
      // Closed
    }, (reason) => {
      // Dismissed
    });
  }

  deactivateModal() {
    this.active = false;
  }
}