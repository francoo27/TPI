import { Component } from '@angular/core';
import { SERVER_API_URL } from 'src/app/app.constants';
import { IPelicula } from '../pelicula/pelicula.model';
import { PeliculaService } from '../pelicula/pelicula.service';

@Component({
    selector: 'car-home',
    templateUrl: './home.component.html',
    providers: []
})
export class HomeComponent {

    peliculas: IPelicula[] = [];
    images: IDataCarousel[] = [
        {
            "previewImageSrc": "http://192.168.0.10:5000/api/img/2",
            "thumbnailImageSrc": "http://192.168.0.10:5000/api/img/2",
            "alt": "Description for Image 1",
            "title": "Title 1"
        }
    ];

    responsiveOptions:any[] = [
        {
            breakpoint: '1024px',
            numVisible: 5
        },
        {
            breakpoint: '768px',
            numVisible: 3
        },
        {
            breakpoint: '560px',
            numVisible: 1
        }
    ];

    constructor(private peliculaService: PeliculaService) { }

    ngOnInit() {
        this.peliculaService.query().subscribe(res => {
            this.peliculas = res.body!
            this.peliculas.forEach(p=>{
                this.images= [...this.images, ...[{
                    previewImageSrc:SERVER_API_URL_IMAGE+'2',
                    thumbnailImageSrc:SERVER_API_URL_IMAGE+'2',
                    alt:p.sinopsis,
                    title:p.tituloPais
                } as IDataCarousel ]]
                console.log(this.images)
            });
        } );

        this.images.push(       {
            "previewImageSrc": "http://192.168.0.10:5000/api/img/2",
            "thumbnailImageSrc": "http://192.168.0.10:5000/api/img/2",
            "alt": "Description for Image 1",
            "title": "Title 1"
        })
    }


}

export const SERVER_API_URL_IMAGE = SERVER_API_URL + 'api/img/'
export interface IDataCarousel {
    previewImageSrc:string
    thumbnailImageSrc:string;
    alt:string;
    title:string;
}
