import { BaseModel } from '../core/components';

export class User extends BaseModel {
    constructor(
        public id: number,
        public first_name: string,
        public middle_name: string,
        public last_name: string,
        public preferences_desc: string,
        public image_mongo_id: string
    ) { super(); }
}