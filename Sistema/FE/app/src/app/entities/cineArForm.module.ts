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
import { ListboxModule } from "primeng/listbox";
import { DropdownModule } from "primeng/dropdown";
import {FileUploadModule} from 'primeng/fileupload';
import {HttpClientModule} from '@angular/common/http';
import {MultiSelectModule} from 'primeng/multiselect';
import {CardModule} from 'primeng/card';

@NgModule({
    imports: [
        InputTextModule,
        InputTextareaModule,
        ButtonModule,
        FormsModule,
        InputNumberModule,
        CheckboxModule,
        CalendarModule,
        InputMaskModule,
        TableModule,
        ListboxModule,
        DropdownModule,
        MultiSelectModule,
        FileUploadModule,
        HttpClientModule,
        CardModule
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
        TableModule,
        ListboxModule,
        DropdownModule,
        MultiSelectModule,
        FileUploadModule,
        HttpClientModule,
        CardModule
    ]
})

export class CineArFormModule{}