import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CascadeSelectModule } from "primeng/cascadeselect";
import {ListboxModule} from 'primeng/listbox';
import {ToastModule} from 'primeng/toast';
import { MessageService } from "primeng/api";
import { CineArFormModule } from "../cineArForm.module";
import { generoRoute } from "./genero.route";
import { GeneroComponent } from "./genero.component";
import { GeneroUpdateComponent } from "./genero-update.component";


const ENTITY_STATES = [...generoRoute]
@NgModule({
    imports: [RouterModule.forChild(ENTITY_STATES),CascadeSelectModule,ListboxModule,ToastModule,CineArFormModule],
    declarations: [
        GeneroComponent,
        GeneroUpdateComponent
        ],
    entryComponents: [],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
    providers: [MessageService]
})
export class CineArGeneroModule{}