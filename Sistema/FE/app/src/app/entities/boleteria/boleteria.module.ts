import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import {ToastModule} from 'primeng/toast';
import { MessageService } from "primeng/api";
import { CineArFormModule } from "../cineArForm.module";
import {GalleriaModule} from 'primeng/galleria';
import { boleteriaRoute } from "./boleteria.route";
import { BoleteriaComponent } from "./boleteria.component";


const ENTITY_STATES = [...boleteriaRoute]
@NgModule({
    imports: [RouterModule.forChild(ENTITY_STATES),ToastModule,CineArFormModule,GalleriaModule],
    declarations: [
        BoleteriaComponent
        ],
    entryComponents: [
        BoleteriaComponent
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
    providers: [MessageService]
})

export class CineArBoleteriaModule{}