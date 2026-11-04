from fastmcp import FastMCP

mcp = FastMCP('amazon Ecommerce')

def search_products():
    ''' The available products in amazon'''
    products = ['Mobiles' , 'Laptops' , 'Fes' , 'Televisions' , 'Air Conditioners' , ' Washing Machinesridg']
    return products

def get_offers():
    ''' This tool gives the offere details on the product'''
    offers = {'Mobiles' : '10%' , 'Laptops' : '15%' , 'Fes' : '20%' , 'Televisions' : '25%' , 'Air Conditioners' : '30%' , ' Washing Machines' : '35%'}
    return offers

def order_status():
    ''' The order status of delivery'''
    return "The product is delevired"


def payment():
    ''' The tool tells whether payment is done or not'''
    status = 'yes'
    return status