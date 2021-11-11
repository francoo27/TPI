import { Injectable } from "@angular/core";
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from "@angular/router";
import { Observable } from "rxjs";
import { AuthService } from "./auth.service";

@Injectable()
export class CanActivateAuth implements CanActivate {
  constructor(
      private authService:AuthService
  ) {}
continue=false;
  canActivate(
  ): Observable<boolean|UrlTree>|Promise<boolean|UrlTree>|boolean|UrlTree {
    this.authService.authenticate({token:localStorage.getItem('token')!}).subscribe(res=> this.continue=true)
    return this.continue;
  }
}

