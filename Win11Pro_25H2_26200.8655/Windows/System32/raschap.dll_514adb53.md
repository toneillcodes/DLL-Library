# Binary Specification: raschap.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\raschap.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `514adb5371a7e7f9ddff4b5c23f8356fcc3621130a0963bd87111bbacf142298`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `RasEapGetIdentity` | `0x3570` | 824 | UnwindData |  |
| 6 | `RasEapCreateConnectionProperties` | `0x3BF0` | 866 | UnwindData |  |
| 2 | `RasEapCreateConnectionPropertiesXml` | `0x57A0` | 9 | UnwindData |  |
| 14 | `RasEapGetInfo` | `0x6D70` | 232 | UnwindData |  |
| 15 | `RasEapGetMethodProperties` | `0x72C0` | 1,531 | UnwindData |  |
| 4 | `RasCpEnumProtocolIds` | `0xE7C0` | 84 | UnwindData |  |
| 9 | `RasEapFreeMemory` | `0xF1A0` | 24 | UnwindData |  |
| 5 | `RasCpGetInfo` | `0x10010` | 136 | UnwindData |  |
| 7 | `RasEapCreateMethodConfiguration` | `0x16AD0` | 407 | UnwindData |  |
| 10 | `RasEapGetConfigBlobAndUserBlob` | `0x16C70` | 396 | UnwindData |  |
| 11 | `RasEapGetCredentials` | `0x16E10` | 508 | UnwindData |  |
| 13 | `RasEapGetIdentityPageGuid` | `0x17020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `RasEapGetNextPageGuid` | `0x17050` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `RasEapInvokeConfigUI` | `0x170A0` | 163 | UnwindData |  |
| 18 | `RasEapInvokeInteractiveUI` | `0x17150` | 152 | UnwindData |  |
| 19 | `RasEapQueryCredentialInputFields` | `0x171F0` | 247 | UnwindData |  |
| 20 | `RasEapQueryInteractiveUIInputFields` | `0x172F0` | 491 | UnwindData |  |
| 21 | `RasEapQueryUIBlobFromInteractiveUIInputFields` | `0x174F0` | 393 | UnwindData |  |
| 22 | `RasEapQueryUserBlobFromCredentialInputFields` | `0x17680` | 665 | UnwindData |  |
| 23 | `RasEapSetRetryFlag` | `0x17920` | 229 | UnwindData |  |
| 1 | `RasEapCreateConnectionProperties2` | `0x1C7B0` | 529 | UnwindData |  |
| 3 | `RasEapCreateUserProperties2` | `0x1C9D0` | 536 | UnwindData |  |
| 8 | `RasEapCreateUserProperties` | `0x1D270` | 294 | UnwindData |  |
