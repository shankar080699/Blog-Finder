import { Component } from '@angular/core';
import {HttpClient,HttpHeaders} from '@angular/common/http';
@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  public title
  api : string[][]
  flag=false
  constructor(private http : HttpClient) {}
  blog(){
    var headers = new Headers();
    const httpOptions = {
      headers : new HttpHeaders({
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      })
    }
  
    let postData = {
            title : this.title,
    }
    this.http.post("http://127.0.0.1:5000/blogs", postData, httpOptions)
      .subscribe(data=>{
              this.api = data as string[][];
              } ,
        (error) => console.log(error)
      )
    this.flag=true
    console.log(this.api[1])
    
  }
}
