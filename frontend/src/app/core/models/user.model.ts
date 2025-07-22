import { UUID } from "./uuid.type";

export interface User {
  id: UUID;
  name: string;
  nickname: string;
  avatar?: string | null;
  followers: UUID[];
  following: UUID[];
  createdAt: Date;
}