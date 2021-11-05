import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CascadeSelectModule } from "primeng/cascadeselect";
import {ListboxModule} from 'primeng/listbox';
import {ToastModule} from 'primeng/toast';
import { MessageService } from "primeng/api";
import { CineArFormModule } from "../cineArForm.module";
import { tecnologiaProyeccionRoute } from "./tecnologia-proyeccion.route";
import { TecnologiaProyeccionComponent } from "./tecnologia-proyeccion.component";
import { TecnologiaProyeccionUpdateComponent } from "./tecnologia-proyeccion-update.component";


const ENTITY_STATES = [...tecnologiaProyeccionRoute]
@NgModule({
    imports: [RouterModule.forChild(ENTITY_STATES),CascadeSelectModule,ListboxModule,ToastModule,CineArFormModule],
    declarations: [
        TecnologiaProyeccionComponent,
        TecnologiaProyeccionUpdateComponent
        ],
    entryComponents: [],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
    providers: [MessageService]
})
export class CineArTecnologiaProyeccionModule{}