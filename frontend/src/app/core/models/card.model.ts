import { UUID } from "./uuid.type";

export interface Card {
  id: UUID;
  name: string;
  description?: string;
  link: string;
  owner: UUID;
  createdAt: Date;
  likes: UUID[];
}