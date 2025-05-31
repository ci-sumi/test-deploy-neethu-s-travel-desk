from django.db import models
from accounts.models import Destination
from decimal import Decimal
from django.core.validators import MinValueValidator



class BudgetCalculator(models.Model):
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name="budgets"
    )
    accommodation_cost = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    transportation_cost = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    food_cost = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    activity_cost = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    number_of_adults = models.IntegerField(default=1,validators=[MinValueValidator(0)])
    number_of_infants = models.IntegerField(default=0,validators=[MinValueValidator(0)])

    def total_cost(self):
        """Calculate the total cost based on the inputs."""
        # Ensure all costs are Decimal types
        accommodation_cost = Decimal(self.accommodation_cost)
        transportation_cost = Decimal(self.transportation_cost)
        food_cost = Decimal(self.food_cost)
        activity_cost = Decimal(self.activity_cost)

        # Convert the number of adults to Decimal for calculation
        number_of_adults_decimal = Decimal(self.number_of_adults)

        # Calculate total cost for adults
        total_cost = (
            accommodation_cost +
            transportation_cost +
            food_cost +
            activity_cost
        ) * number_of_adults_decimal

        # Calculate cost for infants (if applicable)
        number_of_infants_decimal = Decimal(self.number_of_infants)
        if number_of_infants_decimal > 0:
            infant_accommodation_food = accommodation_cost + food_cost
            infant_cost = infant_accommodation_food * number_of_infants_decimal
            total_cost += infant_cost

        return total_cost

    def __str__(self):
        return (
            f"Budget for {self.destination} "
            f"(Adults: {self.number_of_adults}, "
            f"Infants: {self.number_of_infants})"
        )
