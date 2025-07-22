import { User } from "./user.model";
import { UUID } from "./uuid.type";

type CardUser = Pick<User, 'id' | 'avatar' | 'nickname'>;

export interface Card {
  id: UUID;
  name: string;
  description?: string;
  link: string;
  owner: CardUser;
  createdAt: Date;
  likes: CardUser[];
}