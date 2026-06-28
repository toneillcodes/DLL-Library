# Binary Specification: WSDApi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WSDApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `814249a00a522f7d414fca48534b835a952c6bcbbf96856faea620d918e474b2`
* **Total Exported Functions:** 46

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 126 | `WSDCreateUdpAddress` | `0x6600` | 60 | UnwindData |  |
| 110 | `WSDCopyEndpoint` | `0xC360` | 677 | UnwindData |  |
| 106 | `WSDXMLCompareNames` | `0x11430` | 2,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `WSDXMLCleanupElement` | `0x11F20` | 29 | UnwindData |  |
| 103 | `WSDCopyNameList` | `0x11F50` | 217 | UnwindData |  |
| 141 | `WSDXMLBuildAnyForSingleElement` | `0x122D0` | 502 | UnwindData |  |
| 130 | `WSDFreeLinkedMemory` | `0x16CF0` | 108 | UnwindData |  |
| 108 | `WSDAttachLinkedMemory` | `0x1D150` | 26 | UnwindData |  |
| 121 | `WSDCreateHttpAddress` | `0x24A50` | 342 | UnwindData |  |
| 143 | `WSDXMLCreateContext` | `0x28850` | 309 | UnwindData |  |
| 128 | `WSDCreateUdpTransport` | `0x2A940` | 215 | UnwindData |  |
| 123 | `WSDCreateHttpTransport` | `0x2CB60` | 710 | UnwindData |  |
| 107 | `WSDAllocateLinkedMemory` | `0x30C60` | 24 | UnwindData |  |
| 145 | `WSDXMLGetValueFromAny` | `0x41600` | 288 | UnwindData |  |
| 109 | `WSDCompareEndpoints` | `0x53D20` | 117 | UnwindData |  |
| 102 | `WSDCancelNetworkChangeNotify` | `0x58C60` | 94 | UnwindData |  |
| 117 | `WSDCreateDiscoveryProvider` | `0x5B9F0` | 438 | UnwindData |  |
| 118 | `WSDCreateDiscoveryProvider2` | `0x5BBB0` | 529 | UnwindData |  |
| 144 | `WSDXMLGetNameFromBuiltinNamespace` | `0x5CD10` | 627 | UnwindData |  |
| 104 | `WSDNotifyNetworkChange` | `0x5D440` | 156 | UnwindData |  |
| 133 | `WSDGenerateRandomDelay` | `0x5E980` | 188 | UnwindData |  |
| 101 | `WSDAddFirewallCheck` | `0x5F170` | 274 | UnwindData |  |
| 127 | `WSDCreateUdpMessageParameters` | `0x5FDA0` | 217 | UnwindData |  |
| 114 | `WSDCreateDeviceProxy` | `0x60B10` | 286 | UnwindData |  |
| 116 | `WSDCreateDeviceProxyAdvanced` | `0x60C40` | 306 | UnwindData |  |
| 115 | `WSDCreateDeviceProxy2` | `0x60D80` | 315 | UnwindData |  |
| 124 | `WSDCreateMetadataAgent` | `0x64ED0` | 338 | UnwindData |  |
| 105 | `WSDRemoveFirewallCheck` | `0x65D80` | 94 | UnwindData |  |
| 139 | `WSDXMLAddChild` | `0x6A260` | 87 | UnwindData |  |
| 140 | `WSDXMLAddSibling` | `0x6B690` | 70 | UnwindData |  |
| 136 | `WSDSetConfigurationOption` | `0x6C450` | 702 | UnwindData |  |
| 129 | `WSDDetachLinkedMemory` | `0x6CE80` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `WSDCreateDeviceHost2` | `0x6D2D0` | 226 | UnwindData |  |
| 135 | `WSDProcessFault` | `0x6E3B0` | 313 | UnwindData |  |
| 125 | `WSDCreateOutboundAttachment` | `0x6EEE0` | 385 | UnwindData |  |
| 111 | `WSDCreateDeviceHost` | `0x7D7B0` | 209 | UnwindData |  |
| 113 | `WSDCreateDeviceHostAdvanced` | `0x7D890` | 228 | UnwindData |  |
| 119 | `WSDCreateDiscoveryPublisher` | `0x86840` | 179 | UnwindData |  |
| 120 | `WSDCreateDiscoveryPublisher2` | `0x86900` | 253 | UnwindData |  |
| 122 | `WSDCreateHttpMessageParameters` | `0x88810` | 260 | UnwindData |  |
| 131 | `WSDGenerateFault` | `0x8D0A0` | 708 | UnwindData |  |
| 132 | `WSDGenerateFaultEx` | `0x8D370` | 436 | UnwindData |  |
| 134 | `WSDGetConfigurationOption` | `0x934A0` | 545 | UnwindData |  |
| 137 | `WSDUriDecode` | `0x944C0` | 649 | UnwindData |  |
| 138 | `WSDUriEncode` | `0x94750` | 339 | UnwindData |  |
| 100 | *Ordinal Only* | `0x9B5A0` | 299 | UnwindData |  |
