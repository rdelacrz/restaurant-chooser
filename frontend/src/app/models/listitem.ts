import { BaseModel } from '../core/components';

export class ListItem extends BaseModel {
    constructor(
        public id: number,
        public item_id: number,
        public item_name: string,
        public item_abbreviation: string,
        public item_type: number
    ) { super(); }
}