import { Schema, model, Document } from "mongoose";
import { genSalt, hash } from "bcryptjs";

export interface IUser extends Document {
  name: string;
  email: string;
  password: string;
  role: "candidate" | "recruiter";
  createdAt: Date;
  updatedAt: Date;
}

const userSchema = new Schema<IUser>(
  {
    name: {
      type: String,
      required: true,
      trim: true,
    },

    email: {
      type: String,
      required: true,
      unique: true,
      lowercase: true,
      trim: true,
    },

    password: {
      type: String,
      required: true,
      select: false,
    },

    role: {
      type: String,
      enum: ["candidate", "recruiter"],
      required: true,
      default: "candidate",
    },
  },
  {
    timestamps: true,
  },
);

userSchema.pre("save", async function (next) {
  if (!this.isModified("password")) {
    return;
  }

  const salt = await genSalt(10);
  this.password = await hash(this.password, salt);
});

const User = model<IUser>("User", userSchema);

export default User;
