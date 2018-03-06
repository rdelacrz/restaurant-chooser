import { BaseModel } from '../core/components';

export class FileData extends BaseModel {
    constructor(
        public file_name : string,
        public file_type : string,
        public base_64_data : string
    ) { super(); }
}