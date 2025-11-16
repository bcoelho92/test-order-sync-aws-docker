# test-order-sync-aws-docker

# 📁 ESTRUTURA DO PROJETO

```
ordersync/
├── app/
│   ├── api/
│   │   ├── controllers.py
│   │   ├── schemas.py
│   ├── services/
│   │   ├── order_service.py
│   │   ├── external_client.py
│   ├── aws/
│   │   ├── dynamodb.py
│   │   ├── sqs.py
│   │   ├── lambda_handler.py
│   ├── utils/
│   │   ├── logger.py
│   ├── app.py
│   ├── config.py
├── tests/
│   ├── test_orders.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

#  🧠 O QUE O PROJETO FAZ

 * POST /orders → cria pedido
* GET /orders/<id> → busca pedido
* POST /orders/sync → envia pedido para serviço externo

# 