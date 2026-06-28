# Binary Specification: raschap.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\raschap.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6cd8599b00141e09359ea6e27cd7098d50ef0eae1e85ee7a1d15845db1562522`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `RasEapGetIdentity` | `0x3630` | 824 | UnwindData |  |
| 6 | `RasEapCreateConnectionProperties` | `0x3CB0` | 866 | UnwindData |  |
| 2 | `RasEapCreateConnectionPropertiesXml` | `0x5860` | 9 | UnwindData |  |
| 14 | `RasEapGetInfo` | `0x6E30` | 232 | UnwindData |  |
| 15 | `RasEapGetMethodProperties` | `0x7380` | 1,531 | UnwindData |  |
| 4 | `RasCpEnumProtocolIds` | `0xEED0` | 84 | UnwindData |  |
| 9 | `RasEapFreeMemory` | `0xF8B0` | 24 | UnwindData |  |
| 5 | `RasCpGetInfo` | `0x10720` | 136 | UnwindData |  |
| 7 | `RasEapCreateMethodConfiguration` | `0x16BD0` | 407 | UnwindData |  |
| 10 | `RasEapGetConfigBlobAndUserBlob` | `0x16D70` | 396 | UnwindData |  |
| 11 | `RasEapGetCredentials` | `0x16F10` | 508 | UnwindData |  |
| 13 | `RasEapGetIdentityPageGuid` | `0x17120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `RasEapGetNextPageGuid` | `0x17150` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `RasEapInvokeConfigUI` | `0x171A0` | 163 | UnwindData |  |
| 18 | `RasEapInvokeInteractiveUI` | `0x17250` | 152 | UnwindData |  |
| 19 | `RasEapQueryCredentialInputFields` | `0x172F0` | 247 | UnwindData |  |
| 20 | `RasEapQueryInteractiveUIInputFields` | `0x173F0` | 491 | UnwindData |  |
| 21 | `RasEapQueryUIBlobFromInteractiveUIInputFields` | `0x175F0` | 393 | UnwindData |  |
| 22 | `RasEapQueryUserBlobFromCredentialInputFields` | `0x17780` | 665 | UnwindData |  |
| 23 | `RasEapSetRetryFlag` | `0x17A20` | 229 | UnwindData |  |
| 1 | `RasEapCreateConnectionProperties2` | `0x1D2E0` | 529 | UnwindData |  |
| 3 | `RasEapCreateUserProperties2` | `0x1D500` | 536 | UnwindData |  |
| 8 | `RasEapCreateUserProperties` | `0x1DDA0` | 294 | UnwindData |  |
