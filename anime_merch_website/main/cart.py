from .models import Products


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart_session_prods')
        if self.cart is None:
            self.cart = self.session['cart_session_prods'] = {}

    def add(self, product_id, quantity):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        self.cart[product_id]['quantity'] += quantity
        if int(self.cart[product_id]['quantity']) <= 0:
            self.remove(product_id)

    def __iter__(self):
        ids = self.cart.keys()
        products = Products.objects.filter(product_id__in=ids).values()
        for product in products:
            self.cart[str(product['product_id'])].update(product)
        for item in self.cart.values():
            yield item

    def __len__(self):
        return len(self.cart.values())

    def quantity(self, product_id):
        try:
            quantity = self.cart[str(product_id)]['quantity']
        except KeyError:
            quantity = 0
        return quantity

    def remove(self, product_id):
        del self.cart[str(product_id)]

    def clear(self):
        self.cart = self.session['cart_session_prods'] = {}

    def save(self):
        self.session['cart_session_prods'] = self.cart

