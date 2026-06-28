# Binary Specification: computenetwork.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\computenetwork.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fea922c83fa1ad100442c2b5aa1a85b843a01bae99ddb3608a8e8db9da4430ec`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `HcnCloseSdnRoute` | `0x58E0` | 95 | UnwindData |  |
| 2 | `HcnCreateSdnRoute` | `0x5950` | 189 | UnwindData |  |
| 3 | `HcnDeleteSdnRoute` | `0x5A20` | 127 | UnwindData |  |
| 4 | `HcnEnumerateGuestNetworkServices` | `0x5AB0` | 181 | UnwindData |  |
| 5 | `HcnEnumerateSdnRoutes` | `0x5B70` | 181 | UnwindData |  |
| 6 | `HcnModifySdnRoute` | `0x5C30` | 180 | UnwindData |  |
| 7 | `HcnOpenGuestNetworkService` | `0x5CF0` | 178 | UnwindData |  |
| 8 | `HcnOpenSdnRoute` | `0x5DB0` | 178 | UnwindData |  |
| 9 | `HcnQueryGuestNetworkServiceProperties` | `0x5E70` | 239 | UnwindData |  |
| 10 | `HcnQueryMetrics` | `0x5F70` | 181 | UnwindData |  |
| 11 | `HcnQuerySdnRouteProperties` | `0x6030` | 239 | UnwindData |  |
| 12 | `HcnRegisterNetworkCallback` | `0x6130` | 164 | UnwindData |  |
| 13 | `HcnUnregisterNetworkCallback` | `0x61E0` | 91 | UnwindData |  |
| 14 | `HcnCloseEndpoint` | `0x8290` | 95 | UnwindData |  |
| 15 | `HcnCloseGuestNetworkService` | `0x8300` | 95 | UnwindData |  |
| 16 | `HcnCloseLoadBalancer` | `0x8370` | 95 | UnwindData |  |
| 17 | `HcnCloseNamespace` | `0x83E0` | 95 | UnwindData |  |
| 18 | `HcnCloseNetwork` | `0x8450` | 95 | UnwindData |  |
| 19 | `HcnCreateEndpoint` | `0x84C0` | 397 | UnwindData |  |
| 20 | `HcnCreateGuestNetworkService` | `0x8660` | 189 | UnwindData |  |
| 21 | `HcnCreateLoadBalancer` | `0x8730` | 189 | UnwindData |  |
| 22 | `HcnCreateNamespace` | `0x8800` | 189 | UnwindData |  |
| 23 | `HcnCreateNetwork` | `0x88D0` | 189 | UnwindData |  |
| 24 | `HcnDeleteEndpoint` | `0x89A0` | 127 | UnwindData |  |
| 25 | `HcnDeleteGuestNetworkService` | `0x8A30` | 127 | UnwindData |  |
| 26 | `HcnDeleteLoadBalancer` | `0x8AC0` | 127 | UnwindData |  |
| 27 | `HcnDeleteNamespace` | `0x8B50` | 127 | UnwindData |  |
| 28 | `HcnDeleteNetwork` | `0x8BE0` | 127 | UnwindData |  |
| 29 | `HcnEnumerateEndpoints` | `0x8C70` | 181 | UnwindData |  |
| 30 | `HcnEnumerateGuestNetworkPortReservations` | `0x8D30` | 269 | UnwindData |  |
| 31 | `HcnEnumerateLoadBalancers` | `0x8E50` | 181 | UnwindData |  |
| 32 | `HcnEnumerateNamespaces` | `0x8F10` | 181 | UnwindData |  |
| 33 | `HcnEnumerateNetworks` | `0x8FD0` | 181 | UnwindData |  |
| 34 | `HcnFreeGuestNetworkPortReservations` | `0x9090` | 20 | UnwindData |  |
| 35 | `HcnModifyEndpoint` | `0x90B0` | 180 | UnwindData |  |
| 36 | `HcnModifyGuestNetworkService` | `0x9170` | 180 | UnwindData |  |
| 37 | `HcnModifyLoadBalancer` | `0x9230` | 180 | UnwindData |  |
| 38 | `HcnModifyNamespace` | `0x92F0` | 180 | UnwindData |  |
| 39 | `HcnModifyNetwork` | `0x93B0` | 180 | UnwindData |  |
| 40 | `HcnOpenEndpoint` | `0x9470` | 178 | UnwindData |  |
| 41 | `HcnOpenLoadBalancer` | `0x9530` | 178 | UnwindData |  |
| 42 | `HcnOpenNamespace` | `0x95F0` | 178 | UnwindData |  |
| 43 | `HcnOpenNetwork` | `0x96B0` | 178 | UnwindData |  |
| 44 | `HcnQueryEndpointAddresses` | `0x9770` | 239 | UnwindData |  |
| 45 | `HcnQueryEndpointProperties` | `0x9870` | 239 | UnwindData |  |
| 46 | `HcnQueryEndpointStats` | `0x9970` | 239 | UnwindData |  |
| 47 | `HcnQueryFeatures` | `0x9A70` | 243 | UnwindData |  |
| 48 | `HcnQueryLoadBalancerProperties` | `0x9B70` | 239 | UnwindData |  |
| 49 | `HcnQueryNamespaceProperties` | `0x9C70` | 239 | UnwindData |  |
| 50 | `HcnQueryNetworkProperties` | `0x9D70` | 239 | UnwindData |  |
| 51 | `HcnRegisterGuestNetworkServiceCallback` | `0x9E70` | 164 | UnwindData |  |
| 52 | `HcnRegisterServiceCallback` | `0x9F20` | 352 | UnwindData |  |
| 53 | `HcnReleaseGuestNetworkServicePortReservationHandle` | `0xA090` | 135 | UnwindData |  |
| 54 | `HcnReserveGuestNetworkServicePort` | `0xA120` | 179 | UnwindData |  |
| 55 | `HcnReserveGuestNetworkServicePortRange` | `0xA1E0` | 494 | UnwindData |  |
| 56 | `HcnUnregisterGuestNetworkServiceCallback` | `0xA3E0` | 91 | UnwindData |  |
| 57 | `HcnUnregisterServiceCallback` | `0xA450` | 183 | UnwindData |  |
