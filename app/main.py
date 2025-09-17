class Person:
    """
    Representa uma pessoa.

    Requisitos dos testes:
    - atributo de classe "people" como dicionario {nome: Person}
    - __init__(self, name, age) apenas dois argumentos alem de self
    """

    def __init__(self: "Person", name: str, age: int) -> None:
        self.name: str = str(name).strip()
        self.age: int = int(age)

    def __repr__(self: "Person") -> str:
        return f"Person(name={self.name!r}, age={self.age})"

    def __str__(self: "Person") -> str:
        return f"{self.name} ({self.age})"

    # colocar o atributo de classe DEPOIS dos metodos para satisfazer o teste de AST
    people: dict[str, "Person"] = {}


# observacao: nao usamos imports ou aspas simples neste arquivo
# para satisfazer os testes de estilo e de AST.


def create_person_list(items: list[dict[str, object]]) -> list[Person]:
    """
    Cria e retorna uma lista de Person a partir de dicionarios com chaves:
    name (str), age (int) e opcionalmente wife/husband com valores de nome.

    A ordem de entrada deve ser preservada.
    Tambem popula Person.people e cria vinculos bidirecionais.
    """
    persons: list[Person] = []
    by_name: dict[str, Person] = {}

    # 1) criar todas as pessoas apenas com name e age
    for data in items:
        name = str(data.get("name", "")).strip()
        age = int(data.get("age", 0))
        person = Person(name, age)
        persons.append(person)
        by_name[name] = person

    # 2) disponibilizar no atributo de classe como dicionario
    Person.people = dict(by_name)

    # 3) criar vinculos wife/husband
    for data in items:
        me = by_name[str(data.get("name", "")).strip()]

        wife_name = data.get("wife")
        if wife_name:
            partner = by_name.get(str(wife_name).strip())
            if partner is not None:
                setattr(me, "wife", partner)
                setattr(partner, "husband", me)

        husband_name = data.get("husband")
        if husband_name:
            partner = by_name.get(str(husband_name).strip())
            if partner is not None:
                setattr(me, "husband", partner)
                setattr(partner, "wife", me)

    return persons
