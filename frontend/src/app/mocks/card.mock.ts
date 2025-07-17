import { v4 as uuidv4 } from 'uuid';
import { MOCK_USERS } from './users.mock';
import { Card, UUID } from '../core/models';


export const MOCK_CARDS: Card[] = [
  {
    id: uuidv4() as UUID,
    name: 'Закат в горах',
    description: 'Фото с похода в Альпы',
    link: '/assets/cards/1.jpg',
    owner: MOCK_USERS[0].id,
    likes: [MOCK_USERS[1].id],
    createdAt: new Date(2025, 6, 5, 15, 0, 0),
  },
  {
    id: uuidv4() as UUID,
    name: 'Морское побережье',
    description: 'Отдых на Бали',
    link: '/assets/cards/2.jpg',
    owner: MOCK_USERS[1].id,
    likes: [MOCK_USERS[0].id, MOCK_USERS[2].id],
    createdAt: new Date(2025, 6, 6, 11, 20, 0),
  },
  {
    id: uuidv4() as UUID,
    name: 'Городская архитектура',
    link: '/assets/cards/3.jpg',
    owner: MOCK_USERS[2].id,
    likes: [],
    createdAt: new Date(2025, 6, 7, 14, 45, 0),
  },
  {
    id: uuidv4() as UUID,
    name: 'Лесной водопад',
    description: 'Поход в Карелию',
    link: '/assets/cards/4.jpg',
    owner: MOCK_USERS[0].id,
    likes: [MOCK_USERS[2].id],
    createdAt: new Date(2025, 6, 8, 9, 10, 0),
  },
  {
    id: uuidv4() as UUID,
    name: 'Кофе утром',
    link: '/assets/cards/5.jpg',
    owner: MOCK_USERS[1].id,
    likes: [],
    createdAt: new Date(2025, 6, 9, 8, 0, 0),
  },
];