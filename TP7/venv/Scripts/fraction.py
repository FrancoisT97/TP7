
from tp7 import Fraction

def main():
    try:
        # Créer quelques fractions
        fraction1 = Fraction(1, 0)
        fraction2 = Fraction(3, 4)
        fraction3 = Fraction(8, 4)
        fraction4 = Fraction(8, -10)

        # Afficher les propriétés des fractions
        print("Fractions testées:")
        print(f"Fraction 1: {fraction1.numerator}/{fraction1.denominator}")
        print(f"Fraction 2: {fraction2.numerator}/{fraction2.denominator}")
        print(f"Fraction 3: {fraction3.numerator}/{fraction3.denominator}")
        print(f"Fraction 4: {fraction4.numerator}/{fraction4.denominator}")

        # Utilisation des méthodes de la classe Fraction
        print("Simplification et calcul:")
        print("Simlpification Fraction 1:", fraction1)
        print("Simlpification Fraction 2:", fraction2)
        print("Simlpification Fraction 3:", fraction3)
        print("Simlpification Fraction 4:", fraction4)
        print("Mix de Fraction 1:", fraction1.as_mixed_number())
        print("Mix de Fraction 2:", fraction2.as_mixed_number())
        print("Mix de Fraction 3:", fraction3.as_mixed_number())
        print("Mix de Fraction 4:", fraction4.as_mixed_number())
        print("Addition fraction 3 + fraction 4:", fraction3.__add__(fraction4))
        print("Soustraction fraction 1 - fraction 2:", fraction1.__sub__(fraction2))
        print("Soustraction fraction 3 - fraction 4:", fraction3.__sub__(fraction4))
        print("Multiplication fraction 1 * fraction 2:", fraction1.__mul__(fraction2))
        print("Multiplication fraction 3 * fraction 4:", fraction3.__mul__(fraction4))
        print("Division fraction 1 / fraction 2:", fraction1.__truediv__(fraction2))
        print("Division fraction 4 / fraction 3:", fraction4.__truediv__(fraction3))
        print("Puissance fraction 1 ** fraction 2:", fraction1.__pow__(fraction2))

        # Vérification des propriétés des fractions
        print("propriété:")
        print("Fraction 1 == 0 ?", fraction1.is_zero())
        print("Fraction 2 == integer ?", fraction2.is_integer())
        print("Fraction 1 valeur absolut < 1 ?", fraction1.is_proper())
        print("Fraction 2 numerateur == 1 ?", fraction2.is_unit())
        print("Fraction 1 et fraction 2 adjacent?", fraction1.is_adjacent_to(fraction2))


    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()