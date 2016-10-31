"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *


init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

ans1 = Brand.query.get(8)
print '\n' + 'Query #1 %s' % ans1

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

ans2 = Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()
print '\n' + 'Query #2 %s' % ans2

# Get all models that are older than 1960.

ans3 = Model.query.filter(Model.year < 1960).all()
print '\n' + 'Query #3 %s' % ans3

# Get all brands that were founded after 1920.

ans4 = Brand.query.filter(Brand.founded > 1920).all()
print '\n' + 'Query #4 %s' % ans4

# Get all models with names that begin with "Cor".

ans5 = Model.query.filter(Model.name.like('Cor%')).all()
print '\n' + 'Query #5 %s' %  ans5

# Get all brands that were founded in 1903 and that are not yet discontinued.

ans6 = Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()
print '\n' + 'Query #6 %s' % ans6

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

ans7 = Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued!=None)).all()
print '\n' + 'Query #7 %s' % ans7

# Get all models whose brand_name is not Chevrolet.

ans8 = Model.query.filter(Brand.name!='Chevrolet').all()
print '\n' + 'Query #8 %s' % ans8

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    """Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query."""

    results = Model.query.filter(Model.year==year).all()
    for q in results:
        model_name = q.brand.name
        brand_name = q.brand.brand_name
        headquarter = q.brand.headquarters
        model_info = 'Model: %s, Brand: %s, Headquarters: %s, in %s.' % (model_name,
                                                                         brand_name,
                                                                         headquarter)
        print model_info
    return model_info

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    results = Brand.query.all()
    for brand in brands:
        brand_name = brand.name
        model_name = brand.model.name
        summary = 'Brand: %s \n Model Name: %s' % (brand_name, model_name)

        print summary
    return summary

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

#The return value of this query is a row in the brands table with the data associated with the name 'Ford'.
#It returned as a query object which contains all these values.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

#An association table is the bridge for connecting two associated tables that cannot be directly reference to each other.
#Association tables manage a many-to-many relationship with foreign keys associated with the other two tables as primary keys.
# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):
    """Takes in any string as parameter, and returns a list of objects
    that are brands whose name contains or is equal to the input string.
    """
    mystr = str(mystr)
    results = Brand.query.filter(db.or_name.match('mystr'), Brand.name=='mystr').all()

    return results

def get_models_between(start_year, end_year):
    """Takes in a start year and end year (two integers), and returns a
    list of objects that are models with years that fall between the start year (inclusive)
    and end year (exclusive).
    """

#pseudocode:
#get a query using BETWEEN operators from the two integers and return with a list of objects
    models = Model.query.filter(Model.year <= start_year, Model.year > end_year).all()
