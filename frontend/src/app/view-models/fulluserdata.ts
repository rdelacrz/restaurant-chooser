import { BaseModel } from '../core/components';
import { FileData } from './filedata';

export class FullUserData extends BaseModel {
    constructor(
        public id: number,
        public first_name: string,
        public middle_name: string,
        public last_name: string,
        public preferences_desc: string,
        public file_data: FileData
    ) { super(); }
}