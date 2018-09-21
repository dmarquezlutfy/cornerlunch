# Cornerlunch WIP

## What is this?

A solution to [Cornershop Backend Test](https://github.com/cornershop/backend-test), main requirements are explained over there.

## Solution boundaries and assumptions

* Menus are for lunch and only one menu per day.
* Nora can modify lunch menus, but if someone already requested food she needs to handle it. There are no additional notifications.
* The Slack reminder will be send as soon as possible if a new menu is for *today*, otherwise it will be scheduled and send at first hour in the corresponding day.
* To Nora is irrelevant *who* is requesting *what*, correctness of the orders is more relevant. She writes the type of food in each food container. Also, delivery is done in a single location.
* Cornerlunch do not want to be too intrusive in what their employees are eating, so each food request is anonymous.
* Security of nora.cornerlunch.io do not need to be too strict, it can only be accessed from the internal network (recaptchas, ratelimits, etc. are not included).
* This solution will be treated as *single site*.

## Workflow

* Features are developed inside individual branches and then merged to master.
* Fixes are applied inside its corresponding branch and then merged to master.
* Documentation can be directly pushed to master when its unrelated to specific features.