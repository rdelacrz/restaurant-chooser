export class BaseModel {
    public clear() {
        for (let key of Object.keys(this)) {
            this[key] = null;
        }
    }
}