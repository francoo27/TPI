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
            "previewImageSrc": "http://192.168.0.10:5000/api/img/2.jpeg",
            "thumbnailImageSrc": "http://192.168.0.10:5000/api/img/2.jpeg",
            "alt": "Description for Image 1",
            "title": "Title 1"
        }
    ];
    buffer: IDataCarousel[] = [
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
            // this.peliculas.forEach(p=>{
            //     // this.images.push({
            //     //     previewImageSrc:this.getImageSrc(p.imagen!),
            //     //     thumbnailImageSrc:"",
            //     //     alt:p.sinopsis,
            //     //     title:p.tituloPais
            //     // } as IDataCarousel )
            //     this.images.push(       {
            //         "previewImageSrc": this.getImageSrc(p.imagen!),
            //         "thumbnailImageSrc": "http://192.168.0.10:5000/api/img/2.jpeg",
            //         "alt": p.sinopsis!,
            //         "title": p.tituloPais!
            //     })
            // });
        } );
        // console.log(this.images)
        // this.images.push(       {
        //     "previewImageSrc": this.getImageSrc('2.jpeg'),
        //     "thumbnailImageSrc": "http://192.168.0.10:5000/api/img/2.jpeg",
        //     "alt": "",
        //     "title":" p.tituloPais!"
        // })

    }

    getImageSrc(img:string):string{
        console.log(SERVER_API_URL_IMAGE+img)
        return SERVER_API_URL_IMAGE+img;
    }

}



export const SERVER_API_URL_IMAGE = SERVER_API_URL + 'api/img/'
export interface IDataCarousel {
    previewImageSrc:string
    thumbnailImageSrc:string;
    alt:string;
    title:string;
}
