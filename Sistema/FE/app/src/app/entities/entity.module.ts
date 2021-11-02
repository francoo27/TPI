import { NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
@NgModule({
    imports: [
        RouterModule.forChild(
            [
                {
                    path: '', children: [
                        {
                            path: '',
                            loadChildren: () => import('./home/home.module').then(m => m.CineArHomeModule)
                        },
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
                        },
                        {
                            path: 'auth',
                            loadChildren: () => import('../auth/auth.module').then(m => m.CineArAuthModule)
                        },
                        {
                            path: 'boleteria',
                            loadChildren: () => import('./boleteria/boleteria.module').then(m => m.CineArBoleteriaModule)
                        },
                        {
                            path: 'genero',
                            loadChildren: () => import('./genero/genero.module').then(m => m.CineArGeneroModule)
                        },
                        {
                            path: 'clasificacion',
                            loadChildren: () => import('./clasificacion/clasificacion.module').then(m => m.CineArClasificacionModule)
                        }
                    ]
                }
            ]
        )
    ]
})
export class CineArEntityModule{}