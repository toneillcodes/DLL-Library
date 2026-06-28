# Binary Specification: rastls.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rastls.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `20d3e693abb6b46dc7d9bb3ccd13c67d45aafc17dd217e1b108caa8f55021660`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `RasEapCreateConnectionProperties` | `0x4CF0` | 558 | UnwindData |  |
| 4 | `RasEapCreateConnectionPropertiesXml` | `0x4F30` | 902 | UnwindData |  |
| 15 | `RasEapGetMethodProperties` | `0x1D910` | 290 | UnwindData |  |
| 12 | `RasEapGetIdentity` | `0x239D0` | 376 | UnwindData |  |
| 14 | `RasEapGetInfo` | `0x24700` | 294 | UnwindData |  |
| 9 | `RasEapFreeMemory` | `0x24830` | 24 | UnwindData |  |
| 23 | `RasEapSetRetryFlag` | `0x26240` | 86 | UnwindData |  |
| 1 | `EapTls_SaveUserCredentials` | `0x5BBA0` | 498 | UnwindData |  |
| 10 | `RasEapGetConfigBlobAndUserBlob` | `0x5BE10` | 180 | UnwindData |  |
| 11 | `RasEapGetCredentials` | `0x5BED0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `RasEapGetIdentityPageGuid` | `0x5BF30` | 190 | UnwindData |  |
| 16 | `RasEapGetNextPageGuid` | `0x5C000` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `RasEapInvokeConfigUI` | `0x5C080` | 58 | UnwindData |  |
| 18 | `RasEapInvokeInteractiveUI` | `0x5C0C0` | 742 | UnwindData |  |
| 19 | `RasEapQueryCredentialInputFields` | `0x5C3B0` | 94 | UnwindData |  |
| 20 | `RasEapQueryInteractiveUIInputFields` | `0x5C420` | 89 | UnwindData |  |
| 21 | `RasEapQueryUIBlobFromInteractiveUIInputFields` | `0x5C480` | 144 | UnwindData |  |
| 22 | `RasEapQueryUserBlobFromCredentialInputFields` | `0x5C520` | 440 | UnwindData |  |
| 27 | `RasEapUpdateServerConfig` | `0x5C6E0` | 295 | UnwindData |  |
| 3 | `RasEapCreateConnectionProperties2` | `0x63670` | 487 | UnwindData |  |
| 5 | `RasEapCreateMethodConfiguration` | `0x63860` | 232 | UnwindData |  |
| 6 | `RasEapCreateUserProperties` | `0x63950` | 283 | UnwindData |  |
| 7 | `RasEapCreateUserProperties2` | `0x63A80` | 510 | UnwindData |  |
| 8 | `RasEapDeleteTimeStampWchar` | `0x67000` | 561 | UnwindData |  |
| 24 | `RasEapSetTimeStampChar` | `0x67240` | 78 | UnwindData |  |
| 25 | `RasEapSetTimeStampWchar` | `0x672A0` | 624 | UnwindData |  |
| 26 | `RasEapSortRasEntries` | `0x67520` | 1,185 | UnwindData |  |
