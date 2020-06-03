myList = [
    {"count":1,"price":14.5,"title":"商品一"},
    {"count":3,"price":19.5,"title":"商品二"},
    {"count":4,"price":12.5,"title":"商品三"}
]

def cala():
    total = 0
    for tmp in myList:
        total += tmp['price']
    return total