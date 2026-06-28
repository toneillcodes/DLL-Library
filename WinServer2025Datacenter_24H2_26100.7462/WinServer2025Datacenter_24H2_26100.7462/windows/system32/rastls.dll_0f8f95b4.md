# Binary Specification: rastls.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rastls.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0f8f95b427aad4fcb0f4a99f505110a55798c9227f80add8d3f32019d6708631`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `RasEapCreateConnectionProperties` | `0x38A0` | 558 | UnwindData |  |
| 4 | `RasEapCreateConnectionPropertiesXml` | `0x3AE0` | 902 | UnwindData |  |
| 15 | `RasEapGetMethodProperties` | `0x1C4A0` | 290 | UnwindData |  |
| 12 | `RasEapGetIdentity` | `0x22C50` | 376 | UnwindData |  |
| 14 | `RasEapGetInfo` | `0x23980` | 294 | UnwindData |  |
| 9 | `RasEapFreeMemory` | `0x23AB0` | 24 | UnwindData |  |
| 23 | `RasEapSetRetryFlag` | `0x25B50` | 86 | UnwindData |  |
| 1 | `EapTls_SaveUserCredentials` | `0x5D270` | 498 | UnwindData |  |
| 10 | `RasEapGetConfigBlobAndUserBlob` | `0x5D4E0` | 180 | UnwindData |  |
| 11 | `RasEapGetCredentials` | `0x5D5A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `RasEapGetIdentityPageGuid` | `0x5D600` | 190 | UnwindData |  |
| 16 | `RasEapGetNextPageGuid` | `0x5D6D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `RasEapInvokeConfigUI` | `0x5D750` | 58 | UnwindData |  |
| 18 | `RasEapInvokeInteractiveUI` | `0x5D790` | 751 | UnwindData |  |
| 19 | `RasEapQueryCredentialInputFields` | `0x5DA90` | 94 | UnwindData |  |
| 20 | `RasEapQueryInteractiveUIInputFields` | `0x5DB00` | 89 | UnwindData |  |
| 21 | `RasEapQueryUIBlobFromInteractiveUIInputFields` | `0x5DB60` | 144 | UnwindData |  |
| 22 | `RasEapQueryUserBlobFromCredentialInputFields` | `0x5DC00` | 440 | UnwindData |  |
| 27 | `RasEapUpdateServerConfig` | `0x5DDC0` | 295 | UnwindData |  |
| 3 | `RasEapCreateConnectionProperties2` | `0x64E20` | 487 | UnwindData |  |
| 5 | `RasEapCreateMethodConfiguration` | `0x65010` | 232 | UnwindData |  |
| 6 | `RasEapCreateUserProperties` | `0x65100` | 283 | UnwindData |  |
| 7 | `RasEapCreateUserProperties2` | `0x65230` | 510 | UnwindData |  |
| 8 | `RasEapDeleteTimeStampWchar` | `0x687B0` | 561 | UnwindData |  |
| 24 | `RasEapSetTimeStampChar` | `0x689F0` | 78 | UnwindData |  |
| 25 | `RasEapSetTimeStampWchar` | `0x68A50` | 624 | UnwindData |  |
| 26 | `RasEapSortRasEntries` | `0x68CD0` | 1,185 | UnwindData |  |
