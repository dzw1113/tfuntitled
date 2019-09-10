def estimate_house_sales_price(num_of_bedrooms, sqft, neighborhood):
    price = 0

    # a little pinch of this
    price += num_of_bedrooms * 1.0

    # and a big pinch of that
    price += sqft * 1.0

    # maybe a handful of this
    price += neighborhood * 1.0

    # and finally, just a little extra salt for good measure
    price += 1.0

    return price

estimate_house_sales_price(3,2000,'N')