from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "email" VARCHAR(100) NOT NULL UNIQUE;
        ALTER TABLE "users" RENAME COLUMN "password" TO "password_hash";
        CREATE UNIQUE INDEX "uid_users_email_133a6f" ON "users" ("email");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_users_email_133a6f";
        ALTER TABLE "users" RENAME COLUMN "password_hash" TO "password";
        ALTER TABLE "users" DROP COLUMN "email";"""
