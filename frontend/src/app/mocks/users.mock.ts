import { v4 as uuidv4 } from 'uuid';

/**
 * Добавить модели когда будут готовы
 */
export const MOCK_USERS: any[] = [
  {
    id: uuidv4(),
    name: 'Иван Петров',
    avatar: '/assets/avatars/avtr-1.jpg',
    followers: [], // Заполнится ниже
    following: [], // Заполнится ниже
    createdAt: new Date(2025, 6, 1, 10, 0, 0),
  },
  {
    id: uuidv4(),
    name: 'Мария Иванова',
    avatar: '/assets/avatars/avtr-2.jpg',
    followers: [],
    following: [],
    createdAt: new Date(2025, 6, 2, 12, 30, 0),
  },
  {
    id: uuidv4(),
    name: 'Алексей Смирнов',
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