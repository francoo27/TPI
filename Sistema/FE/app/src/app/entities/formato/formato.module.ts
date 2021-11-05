import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CascadeSelectModule } from "primeng/cascadeselect";
import {ListboxModule} from 'primeng/listbox';
import {ToastModule} from 'primeng/toast';
import { MessageService } from "primeng/api";
import { CineArFormModule } from "../cineArForm.module";
import { formatoRoute } from "./formato.route";
import { FormatoComponent } from "./formato.component";
import { FormatoUpdateComponent } from "./formato-update.component";


const ENTITY_STATES = [...formatoRoute]
@NgModule({
    imports: [RouterModule.forChild(ENTITY_STATES),CascadeSelectModule,ListboxModule,ToastModule,CineArFormModule],
    declarations: [
        FormatoComponent,
        FormatoUpdateComponent
        ],
    entryComponents: [],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
    providers: [MessageService]
})
export class CineArFormatoModule{}