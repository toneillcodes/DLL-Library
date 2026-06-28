# Binary Specification: tdh.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\tdh.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `12bd1b8203e5bacce8f414b0bf73b5926febd308fdbcc471942739aedb533faa`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `TdhGetEventMapInformation` | `0x7160` | 141 | UnwindData |  |
| 19 | `TdhGetEventInformation` | `0xB610` | 245 | UnwindData |  |
| 16 | `TdhFormatProperty` | `0xBF30` | 413 | UnwindData |  |
| 22 | `TdhGetProperty` | `0xD720` | 354 | UnwindData |  |
| 24 | `TdhGetPropertySize` | `0xE210` | 330 | UnwindData |  |
| 10 | `TdhEnumerateProviderFieldInformation` | `0x16F60` | 243 | UnwindData |  |
| 31 | `TdhQueryProviderFieldInformation` | `0x17060` | 277 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x1AC20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x1AC40` | 154 | UnwindData |  |
| 3 | `TdhAggregatePayloadFilters` | `0x1AD80` | 71 | UnwindData |  |
| 5 | `TdhCleanupPayloadEventFilterDescriptor` | `0x1ADD0` | 106 | UnwindData |  |
| 7 | `TdhCreatePayloadFilter` | `0x1AE40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `TdhDeletePayloadFilter` | `0x1AE80` | 94 | UnwindData |  |
| 11 | `TdhEnumerateProviderFilters` | `0x1AEF0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `TdhGetAllEventsInformation` | `0x1AF50` | 124 | UnwindData |  |
| 23 | `TdhGetPropertyOffsetAndSize` | `0x1AFE0` | 209 | UnwindData |  |
| 28 | `TdhLoadManifestFromBinary` | `0x1B0C0` | 54 | UnwindData |  |
| 9 | `TdhEnumerateManifestProviderEvents` | `0x1BAF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `TdhEnumerateProviders` | `0x1BB20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `TdhEnumerateProvidersForDecodingSource` | `0x1BB40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `TdhGetManifestEventInformation` | `0x1BB80` | 76 | UnwindData |  |
| 27 | `TdhLoadManifest` | `0x1BBE0` | 62 | UnwindData |  |
| 29 | `TdhLoadManifestFromMemory` | `0x1BC30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `TdhUnloadManifest` | `0x1BC50` | 62 | UnwindData |  |
| 35 | `TdhUnloadManifestFromMemory` | `0x1BCA0` | 21,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `TdhApplyPayloadFilter` | `0x21100` | 2,154 | UnwindData |  |
| 36 | `TdhValidatePayloadFilter` | `0x21970` | 1,213 | UnwindData |  |
| 14 | `TdhEnumerateRemoteWBEMProviderFieldInformation` | `0x26A30` | 192 | UnwindData |  |
| 15 | `TdhEnumerateRemoteWBEMProviders` | `0x26B00` | 357 | UnwindData |  |
| 32 | `TdhQueryRemoteWBEMProviderFieldInformation` | `0x26C70` | 223 | UnwindData |  |
| 6 | `TdhCloseDecodingHandle` | `0x27350` | 17 | UnwindData |  |
| 18 | `TdhGetDecodingParameter` | `0x27370` | 101 | UnwindData |  |
| 25 | `TdhGetWppMessage` | `0x273E0` | 30 | UnwindData |  |
| 26 | `TdhGetWppProperty` | `0x27410` | 171 | UnwindData |  |
| 30 | `TdhOpenDecodingHandle` | `0x274D0` | 157 | UnwindData |  |
| 33 | `TdhSetDecodingParameter` | `0x27580` | 184 | UnwindData |  |
