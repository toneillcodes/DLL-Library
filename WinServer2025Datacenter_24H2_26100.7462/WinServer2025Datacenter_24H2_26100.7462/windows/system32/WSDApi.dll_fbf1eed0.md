# Binary Specification: WSDApi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WSDApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fbf1eed0b99000a37b8d1f2b78e411ef1c43fbb10c57b5965abf6e623c2685fd`
* **Total Exported Functions:** 46

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 103 | `WSDCopyNameList` | `0x28D0` | 274 | UnwindData |  |
| 142 | `WSDXMLCleanupElement` | `0x29F0` | 29 | UnwindData |  |
| 143 | `WSDXMLCreateContext` | `0xAC70` | 309 | UnwindData |  |
| 110 | `WSDCopyEndpoint` | `0x12470` | 721 | UnwindData |  |
| 126 | `WSDCreateUdpAddress` | `0x173B0` | 60 | UnwindData |  |
| 121 | `WSDCreateHttpAddress` | `0x20A10` | 342 | UnwindData |  |
| 130 | `WSDFreeLinkedMemory` | `0x22990` | 108 | UnwindData |  |
| 108 | `WSDAttachLinkedMemory` | `0x22E40` | 14 | UnwindData |  |
| 107 | `WSDAllocateLinkedMemory` | `0x23D70` | 24 | UnwindData |  |
| 106 | `WSDXMLCompareNames` | `0x315E0` | 10,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `WSDCompareEndpoints` | `0x33FD0` | 117 | UnwindData |  |
| 128 | `WSDCreateUdpTransport` | `0x35220` | 215 | UnwindData |  |
| 123 | `WSDCreateHttpTransport` | `0x37980` | 710 | UnwindData |  |
| 145 | `WSDXMLGetValueFromAny` | `0x3DC10` | 288 | UnwindData |  |
| 141 | `WSDXMLBuildAnyForSingleElement` | `0x45300` | 593 | UnwindData |  |
| 102 | `WSDCancelNetworkChangeNotify` | `0x594F0` | 94 | UnwindData |  |
| 117 | `WSDCreateDiscoveryProvider` | `0x5BBA0` | 438 | UnwindData |  |
| 118 | `WSDCreateDiscoveryProvider2` | `0x5BD60` | 529 | UnwindData |  |
| 144 | `WSDXMLGetNameFromBuiltinNamespace` | `0x5CC40` | 627 | UnwindData |  |
| 104 | `WSDNotifyNetworkChange` | `0x5D370` | 156 | UnwindData |  |
| 133 | `WSDGenerateRandomDelay` | `0x5E980` | 188 | UnwindData |  |
| 101 | `WSDAddFirewallCheck` | `0x5EC50` | 274 | UnwindData |  |
| 127 | `WSDCreateUdpMessageParameters` | `0x5F880` | 217 | UnwindData |  |
| 114 | `WSDCreateDeviceProxy` | `0x607B0` | 286 | UnwindData |  |
| 116 | `WSDCreateDeviceProxyAdvanced` | `0x608E0` | 306 | UnwindData |  |
| 115 | `WSDCreateDeviceProxy2` | `0x60A20` | 315 | UnwindData |  |
| 124 | `WSDCreateMetadataAgent` | `0x653A0` | 338 | UnwindData |  |
| 105 | `WSDRemoveFirewallCheck` | `0x663B0` | 94 | UnwindData |  |
| 139 | `WSDXMLAddChild` | `0x6AC90` | 87 | UnwindData |  |
| 140 | `WSDXMLAddSibling` | `0x6C0C0` | 70 | UnwindData |  |
| 136 | `WSDSetConfigurationOption` | `0x6CEF0` | 702 | UnwindData |  |
| 129 | `WSDDetachLinkedMemory` | `0x6D670` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `WSDCreateDeviceHost2` | `0x6DA50` | 226 | UnwindData |  |
| 135 | `WSDProcessFault` | `0x6EB30` | 313 | UnwindData |  |
| 125 | `WSDCreateOutboundAttachment` | `0x6FC00` | 385 | UnwindData |  |
| 111 | `WSDCreateDeviceHost` | `0x80820` | 209 | UnwindData |  |
| 113 | `WSDCreateDeviceHostAdvanced` | `0x80900` | 228 | UnwindData |  |
| 119 | `WSDCreateDiscoveryPublisher` | `0x88DA0` | 179 | UnwindData |  |
| 120 | `WSDCreateDiscoveryPublisher2` | `0x88E60` | 253 | UnwindData |  |
| 122 | `WSDCreateHttpMessageParameters` | `0x8AE60` | 260 | UnwindData |  |
| 131 | `WSDGenerateFault` | `0x8F9B0` | 850 | UnwindData |  |
| 132 | `WSDGenerateFaultEx` | `0x8FD10` | 556 | UnwindData |  |
| 134 | `WSDGetConfigurationOption` | `0x96270` | 545 | UnwindData |  |
| 137 | `WSDUriDecode` | `0x97290` | 649 | UnwindData |  |
| 138 | `WSDUriEncode` | `0x97520` | 339 | UnwindData |  |
| 100 | *Ordinal Only* | `0x9E370` | 299 | UnwindData |  |
