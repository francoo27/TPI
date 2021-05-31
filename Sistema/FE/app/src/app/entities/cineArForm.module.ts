import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { FormsModule } from "@angular/forms";
import {InputTextModule} from 'primeng/inputtext';
import {InputTextareaModule} from 'primeng/inputtextarea';
import {ButtonModule} from 'primeng/button';
import {InputNumberModule} from 'primeng/inputnumber';
import {CheckboxModule} from 'primeng/checkbox';
import {InputMaskModule} from 'primeng/inputmask';
import {CalendarModule} from 'primeng/calendar';
import {TableModule} from 'primeng/table';

@NgModule({
    imports: [
        InputTextModule,
        InputTextareaModule,
        ButtonModule,
        FormsModule,
        InputNumberModule,
        CheckboxModule,
        InputMaskModule,
        TableModule
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
        CalendarModule,
        TableModule]
})

export class CineArFormModule{}