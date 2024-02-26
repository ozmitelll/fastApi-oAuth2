from tortoise import Model, fields
from passlib.hash import bcrypt
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password_hash = fields.CharField(max_length=255)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

    class Meta:
        table = "users"


User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)
