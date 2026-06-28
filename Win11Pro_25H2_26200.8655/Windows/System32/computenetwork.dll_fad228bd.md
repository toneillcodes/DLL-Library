# Binary Specification: computenetwork.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\computenetwork.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fad228bdb858171c3a2055aa9166307725eaec2173294d2912dda9d4cf049f1f`
* **Total Exported Functions:** 57

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `HcnCloseSdnRoute` | `0x58F0` | 95 | UnwindData |  |
| 2 | `HcnCreateSdnRoute` | `0x5960` | 189 | UnwindData |  |
| 3 | `HcnDeleteSdnRoute` | `0x5A30` | 127 | UnwindData |  |
| 4 | `HcnEnumerateGuestNetworkServices` | `0x5AC0` | 181 | UnwindData |  |
| 5 | `HcnEnumerateSdnRoutes` | `0x5B80` | 181 | UnwindData |  |
| 6 | `HcnModifySdnRoute` | `0x5C40` | 180 | UnwindData |  |
| 7 | `HcnOpenGuestNetworkService` | `0x5D00` | 178 | UnwindData |  |
| 8 | `HcnOpenSdnRoute` | `0x5DC0` | 178 | UnwindData |  |
| 9 | `HcnQueryGuestNetworkServiceProperties` | `0x5E80` | 239 | UnwindData |  |
| 10 | `HcnQueryMetrics` | `0x5F80` | 181 | UnwindData |  |
| 11 | `HcnQuerySdnRouteProperties` | `0x6040` | 239 | UnwindData |  |
| 12 | `HcnRegisterNetworkCallback` | `0x6140` | 164 | UnwindData |  |
| 13 | `HcnUnregisterNetworkCallback` | `0x61F0` | 91 | UnwindData |  |
| 14 | `HcnCloseEndpoint` | `0x82A0` | 95 | UnwindData |  |
| 15 | `HcnCloseGuestNetworkService` | `0x8310` | 95 | UnwindData |  |
| 16 | `HcnCloseLoadBalancer` | `0x8380` | 95 | UnwindData |  |
| 17 | `HcnCloseNamespace` | `0x83F0` | 95 | UnwindData |  |
| 18 | `HcnCloseNetwork` | `0x8460` | 95 | UnwindData |  |
| 19 | `HcnCreateEndpoint` | `0x84D0` | 397 | UnwindData |  |
| 20 | `HcnCreateGuestNetworkService` | `0x8670` | 189 | UnwindData |  |
| 21 | `HcnCreateLoadBalancer` | `0x8740` | 189 | UnwindData |  |
| 22 | `HcnCreateNamespace` | `0x8810` | 189 | UnwindData |  |
| 23 | `HcnCreateNetwork` | `0x88E0` | 189 | UnwindData |  |
| 24 | `HcnDeleteEndpoint` | `0x89B0` | 127 | UnwindData |  |
| 25 | `HcnDeleteGuestNetworkService` | `0x8A40` | 127 | UnwindData |  |
| 26 | `HcnDeleteLoadBalancer` | `0x8AD0` | 127 | UnwindData |  |
| 27 | `HcnDeleteNamespace` | `0x8B60` | 127 | UnwindData |  |
| 28 | `HcnDeleteNetwork` | `0x8BF0` | 127 | UnwindData |  |
| 29 | `HcnEnumerateEndpoints` | `0x8C80` | 181 | UnwindData |  |
| 30 | `HcnEnumerateGuestNetworkPortReservations` | `0x8D40` | 269 | UnwindData |  |
| 31 | `HcnEnumerateLoadBalancers` | `0x8E60` | 181 | UnwindData |  |
| 32 | `HcnEnumerateNamespaces` | `0x8F20` | 181 | UnwindData |  |
| 33 | `HcnEnumerateNetworks` | `0x8FE0` | 181 | UnwindData |  |
| 34 | `HcnFreeGuestNetworkPortReservations` | `0x90A0` | 20 | UnwindData |  |
| 35 | `HcnModifyEndpoint` | `0x90C0` | 180 | UnwindData |  |
| 36 | `HcnModifyGuestNetworkService` | `0x9180` | 180 | UnwindData |  |
| 37 | `HcnModifyLoadBalancer` | `0x9240` | 180 | UnwindData |  |
| 38 | `HcnModifyNamespace` | `0x9300` | 180 | UnwindData |  |
| 39 | `HcnModifyNetwork` | `0x93C0` | 180 | UnwindData |  |
| 40 | `HcnOpenEndpoint` | `0x9480` | 178 | UnwindData |  |
| 41 | `HcnOpenLoadBalancer` | `0x9540` | 178 | UnwindData |  |
| 42 | `HcnOpenNamespace` | `0x9600` | 178 | UnwindData |  |
| 43 | `HcnOpenNetwork` | `0x96C0` | 178 | UnwindData |  |
| 44 | `HcnQueryEndpointAddresses` | `0x9780` | 239 | UnwindData |  |
| 45 | `HcnQueryEndpointProperties` | `0x9880` | 239 | UnwindData |  |
| 46 | `HcnQueryEndpointStats` | `0x9980` | 239 | UnwindData |  |
| 47 | `HcnQueryFeatures` | `0x9A80` | 243 | UnwindData |  |
| 48 | `HcnQueryLoadBalancerProperties` | `0x9B80` | 239 | UnwindData |  |
| 49 | `HcnQueryNamespaceProperties` | `0x9C80` | 239 | UnwindData |  |
| 50 | `HcnQueryNetworkProperties` | `0x9D80` | 239 | UnwindData |  |
| 51 | `HcnRegisterGuestNetworkServiceCallback` | `0x9E80` | 164 | UnwindData |  |
| 52 | `HcnRegisterServiceCallback` | `0x9F30` | 352 | UnwindData |  |
| 53 | `HcnReleaseGuestNetworkServicePortReservationHandle` | `0xA0A0` | 135 | UnwindData |  |
| 54 | `HcnReserveGuestNetworkServicePort` | `0xA130` | 179 | UnwindData |  |
| 55 | `HcnReserveGuestNetworkServicePortRange` | `0xA1F0` | 494 | UnwindData |  |
| 56 | `HcnUnregisterGuestNetworkServiceCallback` | `0xA3F0` | 91 | UnwindData |  |
| 57 | `HcnUnregisterServiceCallback` | `0xA460` | 183 | UnwindData |  |
