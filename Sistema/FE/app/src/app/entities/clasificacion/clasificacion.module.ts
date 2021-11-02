import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CascadeSelectModule } from "primeng/cascadeselect";
import {ListboxModule} from 'primeng/listbox';
import {ToastModule} from 'primeng/toast';
import { MessageService } from "primeng/api";
import { CineArFormModule } from "../cineArForm.module";
import { clasificacionRoute } from "./clasificacion.route";
import { ClasificacionComponent } from "./clasificacion.component";
import { ClasificacionUpdateComponent } from "./clasificacion-update.component";


const ENTITY_STATES = [...clasificacionRoute]
@NgModule({
    imports: [RouterModule.forChild(ENTITY_STATES),CascadeSelectModule,ListboxModule,ToastModule,CineArFormModule],
    declarations: [
        ClasificacionComponent,
        ClasificacionUpdateComponent
        ],
    entryComponents: [],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
    providers: [MessageService]
})
export class CineArClasificacionModule{}