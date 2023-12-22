from django_test_migrations.contrib.unittest_case import MigratorTestCase


class TestB0005(MigratorTestCase):
    migrate_from = [
        ("A", "0004_nothing"),
        ("B", "0004_nothing"),
    ]
    migrate_to = [
        (
            "B",
            "0005_custom_migration",
        ),
    ]

    def prepare(self):
        A = self.old_state.apps.get_model("A", "A")
        B = self.old_state.apps.get_model("B", "B")
        a = A.objects.create(a_field="foo")
        a.full_clean()  # should be ok in current state
        B.objects.create(
            a_foreign_key=a,
        )

    def test_b_0005(self):
        A = self.new_state.apps.get_model("A", "A")
        a = A.objects.first()
        self.assertEqual("bar", a.a_field)
