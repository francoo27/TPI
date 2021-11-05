import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api/menuitem';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'app';

  items: MenuItem[]=[];

  ngOnInit() {
      this.items = [
          {
            label: 'Entidades',
            items: [
              {
                label: 'Funcion',
                items: [
                    {
                        label: 'Nuevo', 
                        icon: 'pi pi-fw pi-plus',
                        routerLink: ['/funcion/new']
                    },
                    {
                      label: 'Listado',
                      icon: 'pi pi-fw pi-eye',
                      routerLink: ['/funcion']
                    }
                ]},
              {
                label: 'Pelicula',
                items: [
                    {
                        label: 'Nuevo', 
                        icon: 'pi pi-fw pi-plus',
                        routerLink: ['/pelicula/new']
                    },
                    {
                      label: 'Listado',
                      icon: 'pi pi-fw pi-eye',
                      routerLink: ['/pelicula']
                    }
                ]},
              {
                label: 'Genero',
                items: [
                    {
                        label: 'Nuevo', 
                        icon: 'pi pi-fw pi-plus',
                        routerLink: ['/genero/new']
                    },
                    {
                      label: 'Listado',
                      icon: 'pi pi-fw pi-eye',
                      routerLink: ['/genero']
                    }
                ]},
              {
                label: 'Clasificacion',
                items: [
                    {
                        label: 'Nuevo', 
                        icon: 'pi pi-fw pi-plus',
                        routerLink: ['/clasificacion/new']
                    },
                    {
                      label: 'Listado',
                      icon: 'pi pi-fw pi-eye',
                      routerLink: ['/clasificacion']
                    }
                ]},
              {
                label: 'Audio',
                items: [
                    {
                        label: 'Nuevo', 
                        icon: 'pi pi-fw pi-plus',
                        routerLink: ['/audio/new']
                    },
                    {
                      label: 'Listado',
                      icon: 'pi pi-fw pi-eye',
                      routerLink: ['/audio']
                    }
                ]},
              {
                label: 'Tecnologia Proyeccion',
                items: [
                    {
                        label: 'Nuevo', 
                        icon: 'pi pi-fw pi-plus',
                        routerLink: ['/tecnologia-proyeccion/new']
                    },
                    {
                      label: 'Listado',
                      icon: 'pi pi-fw pi-eye',
                      routerLink: ['/tecnologia-proyeccion']
                    }
                ]},
              {
                label: 'Pais',
                items: [
                    {
                        label: 'Nuevo', 
                        icon: 'pi pi-fw pi-plus',
                        routerLink: ['/pais/new']
                    },
                    {
                      label: 'Listado',
                      icon: 'pi pi-fw pi-eye',
                      routerLink: ['/pais']
                    }
                ]},
                {
                  label: 'Formato',
                  items: [
                      {
                          label: 'Nuevo', 
                          icon: 'pi pi-fw pi-plus',
                          routerLink: ['/formato/new']
                      },
                      {
                        label: 'Listado',
                        icon: 'pi pi-fw pi-eye',
                        routerLink: ['/formato']
                      }
                  ]}
              ]
          }
      ];
  }
}
