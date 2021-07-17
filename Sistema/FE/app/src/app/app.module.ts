import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
import { CineArEntityModule } from './entities/entity.module';
import { HttpClientModule } from '@angular/common/http';
import { MessagesModule } from 'primeng/messages';
import { MessageModule } from 'primeng/message';
import { ToastModule } from 'primeng/toast';
import {MenubarModule} from 'primeng/menubar';
import { CineArFormModule } from './entities/cineArForm.module';
import { CineArAuthModule } from './auth/auth.module';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule,
    CineArEntityModule,
    MessagesModule,
    MessageModule,
    ToastModule,
    MenubarModule,
    CineArFormModule,
    CineArAuthModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
