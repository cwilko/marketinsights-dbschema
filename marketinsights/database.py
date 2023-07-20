from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from sqlalchemy.orm import sessionmaker
import traceback


class MIDatabase:
    def __init__(
        self,
        dbClass,
        pw,
        host="127.0.0.1",
        port="5432",
        dbName="DEFAULT",
        user="DEFAULT",
    ):
        url = URL.create(
            drivername="postgresql",
            username=user,
            host=host,
            database=dbName,
            password=pw,
            port=port,
        )

        self.dbClass = dbClass
        self.engine = create_engine(url)
        self.session = sessionmaker(bind=self.engine)()

    def createTable(self, metadata):
        metadata.create_all(self.engine)

    def dropTable(self, metadata):
        metadata.create_all(self.engine)

    def addEntry(self, values):
        try:
            entryDetails = self.dbClass(**values)
            self.session.add(propertyDetails)
            self.session.commit()
            print(entryDetails)
        except Exception as e:
            print("Duplicate Entry")
            traceback.print_exc()

    def upsert(self, entries: dict, update=True):
        entries_to_update = 0
        entries_to_put = []

        # Find all rows that needs to be updated and merge
        for each in (
            self.session.query(self.dbClass.id, self.dbClass.created_on)
            .filter(self.dbClass.id.in_(entries.keys()))
            .all()
        ):
            values = entries.pop(each.id)
            values["created_on"] = each.created_on  # Preserve field
            entries_to_update += 1
            if update:
                self.session.merge(self.dbClass(**values))

        # Bulk mappings for everything that needs to be inserted
        for entry in entries.values():
            entries_to_put.append(entry)

        self.session.bulk_insert_mappings(self.dbClass, entries_to_put)
        self.session.commit()

        return {"inserted": len(entries_to_put), "updated": entries_to_update}
