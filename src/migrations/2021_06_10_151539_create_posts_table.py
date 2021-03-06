# pylint: disable=missing-module-docstring
from orator.migrations import Migration


class CreatePostsTable(Migration):
    # pylint: disable=missing-class-docstring
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("posts") as table:
            table.increments("id")
            table.timestamps()
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")
            table.string("title")
            table.text("body")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("posts")
