import { NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
@NgModule({
    imports: [
        RouterModule.forChild(
            [
                {
                    path: '', children: [
                        {
                            path: 'pais',
                            loadChildren: () => import('./pais/pais.module').then(m => m.CineArPaisModule)
                        },
                        {
                            path: 'funcion',
                            loadChildren: () => import('./funcion/funcion.module').then(m => m.CineArFuncionModule)
                        },
                        {
                            path: 'pelicula',
                            loadChildren: () => import('./pelicula/pelicula.module').then(m => m.CineArPeliculaModule)
                        }
                    ]
                }
            ]
        )
    ]
})
export class CineArEntityModule{}