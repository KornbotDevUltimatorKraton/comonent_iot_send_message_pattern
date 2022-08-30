json = {
    "category": [{
        "title": "Customer Satisfaction",
        "id": "nnanet:category/certified-pre-owned",
        "items": [{
            "title": "Bulletins",
            "id": "nnanet:category/customer-satisfaction/bulletins",
            "thirditems": [{
                "title": "TOI",
                "id": "nnanet:category/retailer-digital-marketing/toi"
            }, {
                "title": "TOI",
                "id": "nnanet:category/retailer-digital-marketing/toi"
            }]
        }, {
            "title": "Consumer Affairs",
            "id": "nnanet:category/customer-satisfaction/consumer-affairs"
        }, {
            "title": "Loyalty",
            "id": "nnanet:category/customer-satisfaction/loyalty",
            "thirditems": [{
                "title": "TOI",
                "id": "nnanet:category/retailer-digital-marketing/toi"
            }, {
                "title": "TOI",
                "id": "nnanet:category/retailer-digital-marketing/toi"
            }]
        }]
    }, {
        "title": "Retailer Digital Marketing",
        "id": "nnanet:category/retailer-digital-marketing",
        "items": [{
            "title": "TOI",
            "id": "nnanet:category/retailer-digital-marketing/toi",
            "thirditems": [{
                "title": "TOI",
                "id": "nnanet:category/retailer-digital-marketing/toi"
            }, {
                "title": "TOI",
                "id": "nnanet:category/retailer-digital-marketing/toi"
            }]
        }, {
            "title": "Basics",
            "id": "nnanet:category/retailer-digital-marketing/reference-guide/basics"
        }, {
            "title": "International",
            "id": "nnanet:category/retailer-digital-marketing/international"
        }]
    }, {
        "title": "Finance Today",
        "id": "nnanet:category/customer-satisfaction/bulletins/finance-today",
        "items": [{
            "title": "TOI",
            "id": "nnanet:category/retailer-digital-marketing/toi",
            "thirditems": [{
                "title": "TOI",
                "id": "nnanet:category/retailer-digital-marketing/toi"
            }, {
                "title": "TOI",
                "id": "nnanet:category/retailer-digital-marketing/toi"
            }]
        }, {
            "title": "Basics",
            "id": "nnanet:category/retailer-digital-marketing/reference-guide/basics"
        }, {
            "title": "International",
            "id": "nnanet:category/retailer-digital-marketing/international"
        }]
    }, {
        "title": "Annual",
        "id": "nnanet:category/customer-satisfaction/bulletins/finance-today/revenue/annual",
        "items": [{
            "title": "TOI",
            "id": "nnanet:category/retailer-digital-marketing/toi"
        }, {
            "title": "Basics",
            "id": "nnanet:category/retailer-digital-marketing/reference-guide/basics"
        }, {
            "title": "International",
            "id": "nnanet:category/retailer-digital-marketing/international"
        }]
    }]
}
print(list(json))
inner_list = json.get(list(json)[0]) 
for r in range(0,len(inner_list)):
             print("Category_"+str(r),inner_list[r])
