import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import {ToastModule} from 'primeng/toast';
import { MessageService } from "primeng/api";
import { CineArFormModule } from "../cineArForm.module";
import { homeRoute } from "./home.route";
import { HomeComponent } from "./home.component";
import {GalleriaModule} from 'primeng/galleria';


const ENTITY_STATES = [...homeRoute]
@NgModule({
    imports: [RouterModule.forChild(ENTITY_STATES),ToastModule,CineArFormModule,GalleriaModule],
    declarations: [
        HomeComponent
        ],
    entryComponents: [
        HomeComponent
    ],
    schemas: [CUSTOM_ELEMENTS_SCHEMA],
    providers: [MessageService]
})

export class CineArHomeModule{}