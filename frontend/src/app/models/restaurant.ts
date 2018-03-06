import { BaseModel } from '../core/components';

export class Restaurant extends BaseModel {
    constructor(
        public id: number,
        public name: string,
        public cuisine_type_id: number,
        public address_line: string,
        public city: string,
        public state_id: number,
        public zip: string,
        public phone_number: string,
        public suggester_id: number
    ) { super(); }
}