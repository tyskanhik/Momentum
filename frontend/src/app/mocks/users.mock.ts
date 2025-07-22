import { v4 as uuidv4 } from 'uuid';
import { User, UUID } from '../core/models';


export const MOCK_USERS: User[] = [
  {
    id: uuidv4() as UUID,
    name: 'Иван Петров',
    nickname: "ivanpetrov",
    avatar: '/assets/avatars/avtr-1.jpg',
    followers: [], // Заполнится ниже
    following: [], // Заполнится ниже
    createdAt: new Date(2025, 6, 1, 10, 0, 0),
  },
  {
    id: uuidv4() as UUID,
    name: 'Мария Иванова',
    nickname: "mariaivanova",
    avatar: '/assets/avatars/avtr-2.jpg',
    followers: [],
    following: [],
    createdAt: new Date(2025, 6, 2, 12, 30, 0),
  },
  {
    id: uuidv4() as UUID,
    name: 'Алексей Смирнов',
    nickname: "alexsmirnov",
    avatar: null,
    followers: [],
    following: [],
    createdAt: new Date(2025, 6, 3, 9, 15, 0),
  },
];

// Заполняем взаимные подписки
MOCK_USERS[0].followers = [MOCK_USERS[1].id, MOCK_USERS[2].id];
MOCK_USERS[1].followers = [MOCK_USERS[0].id];
MOCK_USERS[2].followers = [MOCK_USERS[0].id];

MOCK_USERS[0].following = [MOCK_USERS[1].id];
MOCK_USERS[1].following = [MOCK_USERS[0].id];