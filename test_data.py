import random

class DataGenerator:
    @staticmethod
    def get_random(n):
        """Ciąg losowy (zawsze ten sam ciąg dla danego n)."""
        state = random.getstate() 
        random.seed(42) 
        data = [random.randint(1, n) for _ in range(n)]
        random.setstate(state) 
        return data

    @staticmethod
    def get_ascending(n):
        """Ciąg rosnący (posortowany)."""
        return list(range(1, n + 1))

    @staticmethod
    def get_descending(n):
        """Ciąg malejący (odwrotnie posortowany)."""
        return list(range(n, 0, -1))

    @staticmethod
    def get_constant(n):
        """Ciąg stały (wszystkie elementy takie same)."""
        return [42] * n

    @staticmethod
    def get_a_shaped(n):
        """Ciąg A-kształtny (nieparzyste rosnąco, parzyste malejąco)."""
        # Lewa strona: liczby nieparzyste od 1 w górę (krok 2)
        left = list(range(1, n + 1, 2))
        
        # Prawa strona: liczby parzyste w dół (krok -2)
        # Zaczynamy od najwyższej parzystej liczby (n lub n-1)
        start_even = n if n % 2 == 0 else n - 1
        right = list(range(start_even, 0, -2))
        
        return left + right

    @classmethod
    def get_all_datasets(cls, n):
        """Zwraca słownik ze wszystkimi zestawami danych dla zadanego N."""
        return {
            "Losowy": cls.get_random(n),
            "Rosnący": cls.get_ascending(n),
            "Malejący": cls.get_descending(n),
            "Stały": cls.get_constant(n),
            "A-kształtny": cls.get_a_shaped(n)
        }