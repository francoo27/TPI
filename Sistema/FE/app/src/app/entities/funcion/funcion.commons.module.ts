import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CascadeSelectModule } from "primeng/cascadeselect";
import { FuncionDetailComponent } from "./funcion-detail.component";
import { FuncionUpdateComponent } from "./funcion-update.component";
import { FuncionComponent } from "./funcion.component";
import {ListboxModule} from 'primeng/listbox';
import {ToastModule} from 'primeng/toast';
import { MessageService } from "primeng/api";
import { CineArFormModule } from "../cineArForm.module";
import { CommonModule } from "@angular/common";

@NgModule({
    imports: [RouterModule,CascadeSelectModule,ListboxModule,ToastModule,CineArFormModule,CommonModule],
    declarations: [
        FuncionComponent,
        FuncionDetailComponent,
        FuncionUpdateComponent
        ],
    entryComponents: [],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
    providers: [MessageService]
})

export class CineArFuncionCommonsModule{}