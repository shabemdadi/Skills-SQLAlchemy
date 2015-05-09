# Note: this file will not run. It is only for recording answers.

# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.

Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != "Chevrolet").all()


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """"Design a function in python that takes in any string as parameter, 
    and returns a list of objects that are brands whose name contains or 
    is equal to the input string."""
    
    Brands = Brand.query.filter(db.or_(Brand.name.like('%'+mystr+'%'),Brand.name == mystr)).all()
    
    return Brands


def get_models_between(start_year, end_year):
    """Design a function that takes in a start year and end year 
    (two integers), and returns a list of objects that are models 
    with years that fall between the start year and end year."""

    Models = Model.query.filter(Model.year > start_year, Model.year < end_year).all()

    return Models

# Part 3: Discussion Questions

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
    
   # There is no returned value, it is a query object.
   
# 2. In your own words, what is an association table, and what *type* of relationship 
# does an association table manage?

    # An association table is a table that is primarily used to map two
    # other tables together, containing foreign keys to those tables. It is used
    # to manage many to many relationships.
