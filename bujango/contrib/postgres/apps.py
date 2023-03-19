from psycopg2.extras import DateRange, DateTimeRange, DateTimeTZRange, NumericRange

from bujango.apps import AppConfig
from bujango.core.signals import setting_changed
from bujango.db import connections
from bujango.db.backends.signals import connection_created
from bujango.db.migrations.writer import MigrationWriter
from bujango.db.models import CharField, OrderBy, TextField
from bujango.db.models.functions import Collate
from bujango.db.models.indexes import IndexExpression
from bujango.utils.translation import gettext_lazy as _

from .indexes import OpClass
from .lookups import SearchLookup, TrigramSimilar, TrigramWordSimilar, Unaccent
from .serializers import RangeSerializer
from .signals import register_type_handlers

RANGE_TYPES = (DateRange, DateTimeRange, DateTimeTZRange, NumericRange)


def uninstall_if_needed(setting, value, enter, **kwargs):
    """
    Undo the effects of PostgresConfig.ready() when bujango.contrib.postgres
    is "uninstalled" by override_settings().
    """
    if (
        not enter
        and setting == "INSTALLED_APPS"
        and "bujango.contrib.postgres" not in set(value)
    ):
        connection_created.disconnect(register_type_handlers)
        CharField._unregister_lookup(Unaccent)
        TextField._unregister_lookup(Unaccent)
        CharField._unregister_lookup(SearchLookup)
        TextField._unregister_lookup(SearchLookup)
        CharField._unregister_lookup(TrigramSimilar)
        TextField._unregister_lookup(TrigramSimilar)
        CharField._unregister_lookup(TrigramWordSimilar)
        TextField._unregister_lookup(TrigramWordSimilar)
        # Disconnect this receiver until the next time this app is installed
        # and ready() connects it again to prevent unnecessary processing on
        # each setting change.
        setting_changed.disconnect(uninstall_if_needed)
        MigrationWriter.unregister_serializer(RANGE_TYPES)


class PostgresConfig(AppConfig):
    name = "bujango.contrib.postgres"
    verbose_name = _("PostgreSQL extensions")

    def ready(self):
        setting_changed.connect(uninstall_if_needed)
        # Connections may already exist before we are called.
        for conn in connections.all(initialized_only=True):
            if conn.vendor == "postgresql":
                conn.introspection.data_types_reverse.update(
                    {
                        3904: "bujango.contrib.postgres.fields.IntegerRangeField",
                        3906: "bujango.contrib.postgres.fields.DecimalRangeField",
                        3910: "bujango.contrib.postgres.fields.DateTimeRangeField",
                        3912: "bujango.contrib.postgres.fields.DateRangeField",
                        3926: "bujango.contrib.postgres.fields.BigIntegerRangeField",
                    }
                )
                if conn.connection is not None:
                    register_type_handlers(conn)
        connection_created.connect(register_type_handlers)
        CharField.register_lookup(Unaccent)
        TextField.register_lookup(Unaccent)
        CharField.register_lookup(SearchLookup)
        TextField.register_lookup(SearchLookup)
        CharField.register_lookup(TrigramSimilar)
        TextField.register_lookup(TrigramSimilar)
        CharField.register_lookup(TrigramWordSimilar)
        TextField.register_lookup(TrigramWordSimilar)
        MigrationWriter.register_serializer(RANGE_TYPES, RangeSerializer)
        IndexExpression.register_wrappers(OrderBy, OpClass, Collate)
