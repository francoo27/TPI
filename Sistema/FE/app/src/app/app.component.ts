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
              label: 'Pais',
              items: [{
                      label: 'Nuevo', 
                      icon: 'pi pi-fw pi-plus',
                      routerLink: ['/pais/new']
                  },
                  {label: 'Listado',
                  icon: 'pi pi-fw pi-eye',
                  routerLink: ['/pais']},
                  {label: 'Quit'}
              ]
          },
          {
              label: 'Edit',
              icon: 'pi pi-fw pi-pencil',
              items: [
                  {label: 'Delete', icon: 'pi pi-fw pi-trash'},
                  {label: 'Refresh', icon: 'pi pi-fw pi-refresh'}
              ]
          }
      ];
  }
}
