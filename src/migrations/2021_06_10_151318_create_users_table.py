# pylint: disable=missing-module-docstring
from orator.migrations import Migration


class CreateUsersTable(Migration):
    # pylint: disable=missing-class-docstring
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.increments("id")
            table.timestamps()
            table.string("name")
            table.text("address")
            table.string("phone_number", 11)
            table.enum("sex", ["male", "female"])

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
