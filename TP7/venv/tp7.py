import math
class Fraction:
    """Class representing a fraction and operations on it

 Date : Aout 2023
 This class allows fraction manipulations through several operations.
 """

    def __init__(self, numerator, denominator):
        """This builds a fraction based on some numerator and denominator.

  PRE : Récupérer deux arguments en paramètres, ils doivent être un nombre entier?
  POST : vérifie le type des paramètre recu sinon renvoie un message d'erreur?
  """
        try :
            if type(numerator) != int or type(denominator) != int:
                raise TypeError("Veuillez entrer des nombres entiers pour le numérateur et le dénominateur")
        except TypeError as e:
            print(e)
        self._numerator = numerator
        self._denominator = denominator

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

  PRE : obtenir la valeur des deux fractions entière à simplifier
  POST : retourner la valeur des fraction simplifier si l'une d'elle est null renvoie 0
  """
        reduced_numerator, reduced_denominator = self.reduce()

        if(reduced_denominator == 1):
            return f"{reduced_numerator}"
        elif (reduced_denominator == 0):
            return f"0"
        else:
            return f"{reduced_numerator}/{reduced_denominator}"

    def reduce(self):
        greatest_common_divisor = self.gcd(self._numerator, self._denominator)
        reduced_numerator = self._numerator // greatest_common_divisor
        reduced_denominator = self._denominator // greatest_common_divisor
        return reduced_numerator, reduced_denominator

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

  A mixed number is the sum of an integer and a proper fraction

  PRE : simplifier les fractions
  POST : retourner le texte contenant la partie entière et la fraction
  """
        if self._denominator != 0:
            reduced_numerator, reduced_denominator = self.reduce()
            whole_part = reduced_numerator // reduced_denominator
            fractional_part_numerator = reduced_numerator % reduced_denominator

            if whole_part == 0:
                return f"{reduced_numerator}/{reduced_denominator}"
            elif fractional_part_numerator == 0:
                return str(whole_part)
            else:
                return f"{whole_part} {fractional_part_numerator}/{reduced_denominator}"
        else :
            return f" la fraction est nul"


    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

   PRE : récupérer les deux valeurs fraction pour les additionner
   POST : retourner la somme des deux fractions en testant si un des numératur ou dénominatuer vaut 0
      """
        new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

        if other._denominator == 0 :
            return Fraction(self._numerator, self._denominator)
        elif self._denominator == 0 :
            return Fraction(other._numerator, other._denominator)
        else :
            new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

  PRE :  récupérer les deux valeurs fraction pour les soustraire
  POST :  retourner la différence entre les deux fractions en testant si un des numératur ou dénominatuer vaut 0
  """
        if other._denominator == 0 :
            return Fraction(self._numerator, self._denominator)
        elif self._denominator == 0 :
            return Fraction(other._numerator, other._denominator)
        else:
            new_numerator = self._numerator * other._denominator - other._numerator * self._denominator
            new_denominator = self._denominator * other._denominator
            return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

  PRE :  récupérer les deux valeurs fraction pour les multiplier
  POST :  retourner le résultat des deux fractions
  """
        new_numerator = self._numerator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

  PRE :  récupérer les deux valeurs fraction pour les diviser
  POST :  retourner le résultat des deux fractions
  """
        new_numerator = self._numerator * other._denominator
        new_denominator = self._denominator * other._numerator
        return Fraction(new_numerator, new_denominator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

  PRE :  récupérer les deux valeurs fraction pour calculer la puissance
  POST :  retourner le résultat de la puissance en vérifiant si un exposant est 0
  """
        if other._denominator == 0:
            return Fraction(self._numerator, self._denominator)
        elif self._denominator == 0:
            return Fraction(other._numerator, other._denominator)
        else:
            new_numerator = self._numerator ** other._numerator
            new_denominator = self._denominator ** other._denominator
            return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

    PRE :  récupérer les deux valeurs fraction pour les comparer
  POST :  retourner vrai (true) si elles sont identiques

  """
        return self._numerator * other._denominator == other._numerator * self._denominator

    def __float__(self):
        """Returns the decimal value of the fraction

    PRE :  récupérer une fraction
  POST :  retourner le resultat en décimale de la fraction
  """
        return self._numerator / self._denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

    PRE :  récupérer une fraction
    POST :  retourner vrai (true) si la fraction vaut 0
  """
        return self._numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

 PRE :  récupérer une fraction
    POST :  retourner vrai (true) si la fraction est de type integer
  """

        if self._denominator == 0:  # Vérification si le dénominateur est zéro
            print("Denominator cannot be zero")

        else :
            return self._numerator % self._denominator  == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

    PRE :  récupérer une fraction
    POST :  retourner vrai (true) si la fraction est absolue
  """
        return abs(self._numerator) < abs(self._denominator)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

    PRE :  récupérer une fraction
    POST :  retourner vrai (true) si le numérateur de la fraction est de 1
  """

        reduced_numerator, _ = self.reduce()
        return reduced_numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

  Two fractions are adjacents if the absolute value of the difference them is a unit fraction

    PRE :  récupérer deux fractions
    POST :  retourner vrai (true) si la différence des deux fraction est une valeur absolue
  """
        difference = self - other
        if math.fabs(difference) == 1:
            return True
        else:
            return False

