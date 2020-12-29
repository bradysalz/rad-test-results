#!/usr/bin/env python3
"""Run this file to create the database.

This holds the models for the database tables.
"""
import peewee

db = peewee.SqliteDatabase('results.db')


class _BaseModel(peewee.Model):
    class Meta:
        database = db


class Part(_BaseModel):
    """A single part, which could have many results."""
    name = peewee.TextField()
    device_type = peewee.TextField()
    manufacturer = peewee.TextField()


class Result(_BaseModel):
    """A radiation test result."""
    # Common test data
    part = peewee.ForeignKeyField(Part, backref='results')
    data_type = peewee.TextField()
    citation = peewee.TextField()

    # Total ionizing dose data
    tid_hdr = peewee.BooleanField(default=False)
    tid_ldr = peewee.BooleanField(default=False)
    tid_proton = peewee.BooleanField(default=False)
    tid_electron = peewee.BooleanField(default=False)

    # Single event effects data
    # Only four characters are used in the collection: HPLN, so that's
    # all we need to store here as well
    see_upset = peewee.FixedCharField(4, default='')
    see_transient = peewee.FixedCharField(4, default='')
    see_fault = peewee.FixedCharField(4, default='')
    see_latchup = peewee.FixedCharField(4, default='')
    see_burnout = peewee.FixedCharField(4, default='')
    see_gate_rupture = peewee.FixedCharField(4, default='')

    # Displacement Damage
    dd_protons = peewee.BooleanField(default=False)
    dd_neutrons = peewee.BooleanField(default=False)


if __name__ == "__main__":
    db.connect()
    db.create_tables([Part, Result])
    db.close()
