import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { FormsModule } from "@angular/forms";
import {InputTextModule} from 'primeng/inputtext';
import {InputTextareaModule} from 'primeng/inputtextarea';
import {ButtonModule} from 'primeng/button';
import {InputNumberModule} from 'primeng/inputnumber';
import {CheckboxModule} from 'primeng/checkbox';
import {InputMaskModule} from 'primeng/inputmask';
import {CalendarModule} from 'primeng/calendar';

@NgModule({
    imports: [
        InputTextModule,
        InputTextareaModule,
        ButtonModule,
        FormsModule,
        InputNumberModule,
        CheckboxModule,
        InputMaskModule
    ],
    declarations: [],
    entryComponents: [],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
    providers: [],
    exports:[
        InputTextModule,
        InputTextareaModule,
        ButtonModule,
        FormsModule,
        InputNumberModule,
        CheckboxModule,
        CalendarModule]
})

export class CineArFormModule{}