"""
easy_tbot is a library and a framework for building Telegram Bots. The library is code and
documented using well curated practices so you should be able to understand wath are we trying
to achieve.
"""

# For a few years, telegram has gained popularity and lately more, mainly due to the different 
# privacy policies between it and its competitors, but also because it is one of the few messaging 
# services that so completely exposes a public API that allows , among other things, the construction of Bots.
# There are several libraries that work as clients of these APIs allowing us to create these bots in our preferred languages.
# These libraries collect the basic functionality to build a bot but do not solve problems that are normally included in this process.

# ### Which leads us to ask ourselves, what do we want when we make a bot?

# There are several things that are wanted when making a bot in telegram and in most three things are required:
#     - Process information
#     - Store information
#     - Show information
    
# Current libraries allow us to process and display information but in the lower layer of what is 
# expected from a bot in Telegram, making the process of creating serious functionalities more 
# complex than just processing simple commands and eventually forcing us to depend on other libraries 
# that they are not part of the Telegram packaging. Hence the idea of ​​making a framework that allows us 
# to make telegram bots with some comfort without rewriting code, using well-equipped libraries for this purpose.

# As you work with the Telegram bots API you realize that it works with an architecture similar to 
# MVC (model view controller) or MVT (model view template) where in the best of cases we make a database (our model ), 
# we process information (our controller) and return an object to Telegram (a message, multimedia, quick view, ... etc, 
# which would be our view or template), but these things are either not well defined or are a bit mixed. 
# The objective of the framework is not only to define well an architecture or pattern that standardizes 
# without losing flexibility the Telegram bot creation process, it is also to offer the developer a higher level layer. 
# All this without discarding or despising the libraries so well made that there are for communication with Telegram but 
# using them and working on a higher layer.