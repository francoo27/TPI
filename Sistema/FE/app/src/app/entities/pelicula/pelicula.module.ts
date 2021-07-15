import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CascadeSelectModule } from "primeng/cascadeselect";
import { PeliculaDetailComponent } from "./pelicula-detail.component";
import { PeliculaUpdateComponent } from "./pelicula-update.component";
import { PeliculaComponent } from "./pelicula.component";
import {ListboxModule} from 'primeng/listbox';
import {ToastModule} from 'primeng/toast';
import { MessageService } from "primeng/api";
import { CineArFormModule } from "../cineArForm.module";
import { peliculaRoute } from "./pelicula.route";

const ENTITY_STATES = [...peliculaRoute]
@NgModule({
    imports: [RouterModule.forChild(ENTITY_STATES),CascadeSelectModule,ListboxModule,ToastModule,CineArFormModule],
    declarations: [
        PeliculaComponent,
        PeliculaDetailComponent,
        PeliculaUpdateComponent
        ],
    entryComponents: [],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
    providers: [MessageService]
})

export class CineArPeliculaModule{}