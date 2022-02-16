import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Shipping(Client):
    """
    Shipping SP-API Client
    :link: 

    Provides programmatic access to Amazon Shipping APIs.
    """


    @sp_endpoint('/shipping/v1/shipments', method='POST')
    def create_shipment(self, **kwargs) -> ApiResponse:
        """
        create_shipment(self, **kwargs) -> ApiResponse

        Create a new shipment.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 5 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The request schema for the createShipment operation.',
 'properties': {'clientReferenceId': {'$ref': '#/definitions/ClientReferenceId'}, 'containers': {'$ref': '#/definitions/ContainerList'}, 'shipFrom': {'$ref': '#/definitions/Address'}, 'shipTo': {'$ref': '#/definitions/Address'}},
 'required': ['clientReferenceId', 'containers', 'shipFrom', 'shipTo'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/shipping/v1/shipments/{}', method='GET')
    def get_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        get_shipment(self, shipmentId, **kwargs) -> ApiResponse

        Return the entire shipment object for the shipmentId.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 5 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            shipmentId:string | * REQUIRED 
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), shipmentId), params=kwargs)
    

    @sp_endpoint('/shipping/v1/shipments/{}/cancel', method='POST')
    def cancel_shipment(self, shipmentId, **kwargs) -> ApiResponse:
        """
        cancel_shipment(self, shipmentId, **kwargs) -> ApiResponse

        Cancel a shipment by the given shipmentId.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 5 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            shipmentId:string | * REQUIRED 
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), shipmentId), data=kwargs)
    

    @sp_endpoint('/shipping/v1/shipments/{}/purchaseLabels', method='POST')
    def purchase_labels(self, shipmentId, **kwargs) -> ApiResponse:
        """
        purchase_labels(self, shipmentId, **kwargs) -> ApiResponse

        Purchase shipping labels based on a given rate.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 5 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            shipmentId:string | * REQUIRED 
        
            body: | * REQUIRED {'description': 'The request schema for the purchaseLabels operation.',
 'properties': {'labelSpecification': {'$ref': '#/definitions/LabelSpecification'}, 'rateId': {'$ref': '#/definitions/RateId'}},
 'required': ['labelSpecification', 'rateId'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), shipmentId), data=kwargs)
    

    @sp_endpoint('/shipping/v1/shipments/{}/label', method='POST')
    def retrieve_shipping_label(self, shipmentId, **kwargs) -> ApiResponse:
        """
        retrieve_shipping_label(self, shipmentId, **kwargs) -> ApiResponse

        Retrieve shipping label based on the shipment id and tracking id.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 5 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            shipmentId:string | * REQUIRED 
        
            trackingId:string | * REQUIRED 
        
            body: | * REQUIRED {'description': 'The request schema for the retrieveShippingLabel operation.', 'properties': {'labelSpecification': {'$ref': '#/definitions/LabelSpecification'}}, 'required': ['labelSpecification'], 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), shipmentId), data=kwargs)
    

    @sp_endpoint('/shipping/v1/purchaseShipment', method='POST')
    def purchase_shipment(self, **kwargs) -> ApiResponse:
        """
        purchase_shipment(self, **kwargs) -> ApiResponse

        Purchase shipping labels.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 5 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The payload schema for the purchaseShipment operation.',
 'properties': {'clientReferenceId': {'$ref': '#/definitions/ClientReferenceId'},
                'containers': {'$ref': '#/definitions/ContainerList'},
                'labelSpecification': {'$ref': '#/definitions/LabelSpecification'},
                'serviceType': {'$ref': '#/definitions/ServiceType'},
                'shipDate': {'description': 'The start date and time. This defaults to the current date and time.', 'format': 'date-time', 'type': 'string'},
                'shipFrom': {'$ref': '#/definitions/Address'},
                'shipTo': {'$ref': '#/definitions/Address'}},
 'required': ['clientReferenceId', 'containers', 'labelSpecification', 'serviceType', 'shipFrom', 'shipTo'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/shipping/v1/rates', method='POST')
    def get_rates(self, **kwargs) -> ApiResponse:
        """
        get_rates(self, **kwargs) -> ApiResponse

        Get service rates.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 5 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'The payload schema for the getRates operation.',
 'properties': {'containerSpecifications': {'$ref': '#/definitions/ContainerSpecificationList'},
                'serviceTypes': {'$ref': '#/definitions/ServiceTypeList'},
                'shipDate': {'description': 'The start date and time. This defaults to the current date and time.', 'format': 'date-time', 'type': 'string'},
                'shipFrom': {'$ref': '#/definitions/Address'},
                'shipTo': {'$ref': '#/definitions/Address'}},
 'required': ['containerSpecifications', 'serviceTypes', 'shipFrom', 'shipTo'],
 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/shipping/v1/account', method='GET')
    def get_account(self, **kwargs) -> ApiResponse:
        """
        get_account(self, **kwargs) -> ApiResponse

        Verify if the current account is valid.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 5 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/shipping/v1/tracking/{}', method='GET')
    def get_tracking_information(self, trackingId, **kwargs) -> ApiResponse:
        """
        get_tracking_information(self, trackingId, **kwargs) -> ApiResponse

        Return the tracking information of a shipment.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 1 | 1 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            trackingId:string | * REQUIRED 
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), trackingId), params=kwargs)

    @sp_endpoint('/easyship/v0/timeSlots', method='POST')
    def get_time_slots(self, **kwargs) -> ApiResponse:
        """
        Raw request:
            {
              "marketplaceId": "string",
              "amazonOrderId": "string",
              "packageDimensions": {
                "length": 0.01,
                "width": 0.01,
                "height": 0.01,
                "unit": "cm",
                "identifier": "string"
              },
              "packageWeight": {
                "value": 11,
                "unit": "grams"
              }
            }
        Response:
            {
              "payload": {
                "amazonOrderId": "string",
                "timeSlotList": [
                  {
                    "slotId": "string",
                    "startTime": "2022-02-15T09:49:50.875Z",
                    "endTime": "2022-02-15T09:49:50.875Z",
                    "handoverMethod": "PICKUP"
                  }
                ]
              },
              "errors": [
                {
                  "code": "InvalidInput",
                  "message": "string",
                  "details": "string"
                }
              ]
            }
        """
        return self._request(fill_query_params(kwargs.pop('path')), data=kwargs)

    @sp_endpoint('/easyship/v0/packages', method='GET')
    def get_packages(self, **kwargs) -> ApiResponse:
        """
        Raw response:
            {
              "payload": {
                "scheduledPackageId": {
                  "amazonOrderId": "string",
                  "packageId": "string"
                },
                "packageDimensions": {
                  "length": 0.01,
                  "width": 0.01,
                  "height": 0.01,
                  "unit": "cm",
                  "identifier": "string"
                },
                "packageWeight": {
                  "value": 11,
                  "unit": "grams"
                },
                "packageItemList": [
                  {
                    "orderItemId": "string",
                    "orderItemSerialNumberList": [
                      "string"
                    ]
                  }
                ],
                "packageTimeSlot": {
                  "slotId": "string",
                  "startTime": "2022-02-15T10:00:47.380Z",
                  "endTime": "2022-02-15T10:00:47.380Z",
                  "handoverMethod": "PICKUP"
                },
                "packageIdentifier": "string",
                "invoice": {
                  "invoiceNumber": "string",
                  "invoiceDate": "2022-02-15T10:00:47.380Z"
                },
                "packageStatus": "ReadyForPickup",
                "trackingDetails": {
                  "trackingId": "string"
                }
              },
              "errors": [
                {
                  "code": "InvalidInput",
                  "message": "string",
                  "details": "string"
                }
              ]
            }
        """
        return self._request(fill_query_params(kwargs.pop('path')), params=kwargs)

    @sp_endpoint('/easyship/v0/packages', method='POST')
    def create_scheduled_packages(self, **kwargs) -> ApiResponse:
        """
        Raw request:
            {
              "amazonOrderId": "string",
              "marketplaceId": "string",
              "packageRequestDetails": {
                "packageDimensions": {
                  "length": 0.01,
                  "width": 0.01,
                  "height": 0.01,
                  "unit": "cm",
                  "identifier": "string"
                },
                "packageWeight": {
                  "value": 11,
                  "unit": "grams"
                },
                "packageItemList": [
                  {
                    "orderItemId": "string",
                    "orderItemSerialNumberList": [
                      "string"
                    ]
                  }
                ],
                "packageTimeSlot": {
                  "slotId": "string",
                  "startTime": "2022-02-15T07:23:06.795Z",
                  "endTime": "2022-02-15T07:23:06.795Z",
                  "handoverMethod": "PICKUP"
                },
                "packageIdentifier": "string"
              }
            }
        Response:
            {
              "payload": {
                "scheduledPackageId": {
                  "amazonOrderId": "string",
                  "packageId": "string"
                },
                "packageDimensions": {
                  "length": 0.01,
                  "width": 0.01,
                  "height": 0.01,
                  "unit": "cm",
                  "identifier": "string"
                },
                "packageWeight": {
                  "value": 11,
                  "unit": "grams"
                },
                "packageItemList": [
                  {
                    "orderItemId": "string",
                    "orderItemSerialNumberList": [
                      "string"
                    ]
                  }
                ],
                "packageTimeSlot": {
                  "slotId": "string",
                  "startTime": "2022-02-15T10:01:49.901Z",
                  "endTime": "2022-02-15T10:01:49.901Z",
                  "handoverMethod": "PICKUP"
                },
                "packageIdentifier": "string",
                "invoice": {
                  "invoiceNumber": "string",
                  "invoiceDate": "2022-02-15T10:01:49.901Z"
                },
                "packageStatus": "ReadyForPickup",
                "trackingDetails": {
                  "trackingId": "string"
                }
              },
              "errors": [
                {
                  "code": "InvalidInput",
                  "message": "string",
                  "details": "string"
                }
              ]
            }
        """
        return self._request(fill_query_params(kwargs.pop('path')), data=kwargs)

    @sp_endpoint('/easyship/v0/packages', method='PATCH')
    def update_scheduled_packages(self, **kwargs) -> ApiResponse:
        """
        Raw request:
            {
              "marketplaceId": "string",
              "scheduledPackageUpdateDetailsList": [
                {
                  "scheduledPackageId": {
                    "amazonOrderId": "string",
                    "packageId": "string"
                  },
                  "packageTimeSlot": {
                    "slotId": "string",
                    "startTime": "2022-02-15T10:03:59.381Z",
                    "endTime": "2022-02-15T10:03:59.381Z",
                    "handoverMethod": "PICKUP"
                  }
                }
              ]
            }
        Response:
            {
              "payload": [
                {
                  "scheduledPackageId": {
                    "amazonOrderId": "string",
                    "packageId": "string"
                  },
                  "packageDimensions": {
                    "length": 0.01,
                    "width": 0.01,
                    "height": 0.01,
                    "unit": "cm",
                    "identifier": "string"
                  },
                  "packageWeight": {
                    "value": 11,
                    "unit": "grams"
                  },
                  "packageItemList": [
                    {
                      "orderItemId": "string",
                      "orderItemSerialNumberList": [
                        "string"
                      ]
                    }
                  ],
                  "packageTimeSlot": {
                    "slotId": "string",
                    "startTime": "2022-02-15T10:04:42.837Z",
                    "endTime": "2022-02-15T10:04:42.837Z",
                    "handoverMethod": "PICKUP"
                  },
                  "packageIdentifier": "string",
                  "invoice": {
                    "invoiceNumber": "string",
                    "invoiceDate": "2022-02-15T10:04:42.837Z"
                  },
                  "packageStatus": "ReadyForPickup",
                  "trackingDetails": {
                    "trackingId": "string"
                  }
                }
              ],
              "errors": [
                {
                  "code": "InvalidInput",
                  "message": "string",
                  "details": "string"
                }
              ]
            }
        """
        return self._request(fill_query_params(kwargs.pop('path')), data=kwargs)
