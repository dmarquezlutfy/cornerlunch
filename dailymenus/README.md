# DailyMenus Module

## Module functionalities

* Keep models related to Daily Menus
* Admin interface for Daily Menu handling

## Design decisions

* DailyMenu and MenuAlternative was modeled in a one-to-many relationship to keep generality of the solution. Each MenuAlternative could be stored inside a JSONField for each DailyMenu, but JSONField has limited support (depends on database type). Another alternative is to use many-to-many relationship to reuse each MenuAlternative, but there is no clarity in how the user interface should behave.
* If there are 4 menu alternatives on average each day, then in one month there are gonna be 80 new entries in MenuAlternative table. Said growth is not a problem for any database.