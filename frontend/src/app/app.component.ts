import { Component, inject, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CardsService } from './core/services/cards.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'momentum';
  private cardServices =  inject(CardsService)
  cards = signal<any[]>([]) 

  constructor() {
    this.loadData()
  }

  loadData() {
    this.cardServices.getCards().subscribe({
      next: data => this.cards.set(data)
    })
  }

  log() {
    console.log(this.cards());
  }
}
