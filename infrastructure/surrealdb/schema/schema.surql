# This file defines the schema for the SurrealDB database used in the FinWorldModel project.
# It is an initial setup for the database, creating the necessary namespace, database, and tables.
DEFINE NAMESPACE IF NOT EXISTS finworldmodel;
USE NS finworldmodel;

DEFINE DATABASE IF NOT EXISTS research;
USE DB research;

DEFINE TABLE IF NOT EXISTS experiment SCHEMALESS;
DEFINE TABLE IF NOT EXISTS dataset SCHEMALESS;
DEFINE TABLE IF NOT EXISTS financial_entity SCHEMALESS;
DEFINE TABLE IF NOT EXISTS observation SCHEMALESS;
DEFINE TABLE IF NOT EXISTS model_run SCHEMALESS;
