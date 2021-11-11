import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api/menuitem';
import { AuthService } from './auth/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'app';

  items: MenuItem[]=[
    {
      label: 'Cartelera', 
      icon: 'pi pi-fw',
      routerLink: ['']
    },
    {
      label: 'Boleteria', 
      icon: 'pi pi-fw',
      routerLink: ['/boleteria']
    }
  ];

  isLogged:boolean= false
  email!:string
  constructor(
    private authService: AuthService
    ) {}

  ngOnInit() {
    this.authService.authenticate({token:localStorage.getItem('token')!}).subscribe(
      res => {
      this.email=localStorage.getItem('email')!;
      this.items = [...this.items,
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
        },
    ]},
      err => console.log(err)
    )

  }

  logout(){
    this.authService.logout({token:localStorage.getItem('token')!}).subscribe(
      res=> localStorage.clear()
    )
  }
}
