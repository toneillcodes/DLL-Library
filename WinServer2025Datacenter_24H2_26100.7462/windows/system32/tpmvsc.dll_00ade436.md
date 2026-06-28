# Binary Specification: tpmvsc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\tpmvsc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `00ade4366ec10821ed8ab33ec097162fb611e001928daf0194f505f530572ded`
* **Total Exported Functions:** 37

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1CBA0` | 218 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1CC80` | 251 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x1CF20` | 276 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1D040` | 235 | UnwindData |  |
| 5 | `TpmVCardCreate` | `0x31370` | 610 | UnwindData |  |
| 6 | `TpmVCardCreateInProc` | `0x315E0` | 589 | UnwindData |  |
| 7 | `TpmVCardDestroy` | `0x31840` | 382 | UnwindData |  |
| 8 | `TpmVCardDestroyInProc` | `0x319D0` | 383 | UnwindData |  |
| 9 | `VCardAuthenticatePin` | `0x31B60` | 329 | UnwindData |  |
| 10 | `VCardChangePin` | `0x31CB0` | 361 | UnwindData |  |
| 11 | `VCardClose` | `0x31E20` | 373 | UnwindData |  |
| 12 | `VCardCloseChannel` | `0x31FA0` | 279 | UnwindData |  |
| 13 | `VCardCreateClaim` | `0x320C0` | 397 | UnwindData |  |
| 14 | `VCardCreateKey` | `0x32260` | 623 | UnwindData |  |
| 15 | `VCardDeauthenticate` | `0x324E0` | 277 | UnwindData |  |
| 16 | `VCardDecrypt` | `0x32600` | 494 | UnwindData |  |
| 17 | `VCardDeinitialize` | `0x32800` | 366 | UnwindData |  |
| 18 | `VCardDeleteKey` | `0x32980` | 401 | UnwindData |  |
| 19 | `VCardEncrypt` | `0x32B20` | 494 | UnwindData |  |
| 20 | `VCardExportRsaPubKey` | `0x32D20` | 347 | UnwindData |  |
| 21 | `VCardGetAikCertificate` | `0x32E90` | 336 | UnwindData |  |
| 22 | `VCardGetAikContainerName` | `0x32FF0` | 329 | UnwindData |  |
| 23 | `VCardGetChallenge` | `0x33140` | 384 | UnwindData |  |
| 24 | `VCardGetKeyType` | `0x332D0` | 311 | UnwindData |  |
| 25 | `VCardGetPinLength` | `0x33410` | 322 | UnwindData |  |
| 26 | `VCardGetRemainingRetryCount` | `0x33560` | 333 | UnwindData |  |
| 27 | `VCardGetTransportKeyAlg` | `0x336C0` | 151 | UnwindData |  |
| 28 | `VCardImportRsaKey` | `0x33760` | 777 | UnwindData |  |
| 29 | `VCardImportSymKey` | `0x33A70` | 507 | UnwindData |  |
| 30 | `VCardInitialize` | `0x33C80` | 306 | UnwindData |  |
| 31 | `VCardInvalidateChallenge` | `0x33DC0` | 310 | UnwindData |  |
| 32 | `VCardOpen` | `0x33F00` | 394 | UnwindData |  |
| 33 | `VCardOpenChannel` | `0x34090` | 388 | UnwindData |  |
| 34 | `VCardResetPin` | `0x34220` | 329 | UnwindData |  |
| 35 | `VCardSetResponse` | `0x34370` | 379 | UnwindData |  |
| 36 | `VCardSignHash` | `0x34500` | 489 | UnwindData |  |
| 37 | `VCardUnblockPin` | `0x346F0` | 331 | UnwindData |  |
