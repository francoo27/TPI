import { NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { CineArFuncionCommonsModule } from "./funcion.commons.module";
import { funcionRoute } from "./funcion.route";

const ENTITY_STATES = [...funcionRoute]
@NgModule({
    imports: [CineArFuncionCommonsModule, RouterModule.forChild(ENTITY_STATES)]
})
export class CineArFuncionModule{}