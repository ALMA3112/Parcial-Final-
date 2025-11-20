def generar_gramatica_sql_crud():

    g = {
        "Query": {
            "producciones": ["SelectStmt", "InsertStmt", "UpdateStmt", "DeleteStmt"],
            "atributos": {"tipo": "S", "tabla": "S"},
            "acciones": [
                "Query.tipo = producción.tipo",
                "Query.tabla = producción.tabla"
            ]
        },

        "SelectStmt": {
            "producciones": ["SELECT Campos FROM Tabla Cond"],
            "atributos": {"tipo": "S", "tabla": "S", "campos": "S"},
            "acciones": [
                "SelectStmt.tipo = 'SELECT'",
                "SelectStmt.tabla = Tabla.nombre",
                "SelectStmt.campos = Campos.lista"
            ]
        },

        "InsertStmt": {
            "producciones": ["INSERT INTO Tabla VALUES (Valores)"],
            "atributos": {"tipo": "S", "tabla": "S"},
            "acciones": [
                "InsertStmt.tipo = 'INSERT'",
                "InsertStmt.tabla = Tabla.nombre"
            ]
        },

        "UpdateStmt": {
            "producciones": ["UPDATE Tabla SET Asignaciones Cond"],
            "atributos": {"tipo": "S", "tabla": "S"},
            "acciones": [
                "UpdateStmt.tipo = 'UPDATE'",
                "UpdateStmt.tabla = Tabla.nombre"
            ]
        },

        "DeleteStmt": {
            "producciones": ["DELETE FROM Tabla Cond"],
            "atributos": {"tipo": "S", "tabla": "S"},
            "acciones": [
                "DeleteStmt.tipo = 'DELETE'",
                "DeleteStmt.tabla = Tabla.nombre"
            ]
        },
    }

    return g

gram = generar_gramatica_sql_crud()

print("Gramatica sql \n")

for regla, datos in gram.items():
    print(f"\nRegla: {regla}")
    print("  Producciones:", datos["producciones"])
    print("  Atributos:", datos["atributos"])
